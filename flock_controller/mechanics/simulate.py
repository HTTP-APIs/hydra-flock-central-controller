"""Main control loop for drone."""
import threading
from flock_controller.mechanics.main import find_res
import re
from flock_controller.mechanics.anomaly import send_anomaly, get_anomaly_collection, get_anomaly
from flock_controller.mechanics.anomaly import delete_anomaly, update_anomaly
from flock_controller.mechanics.drone import get_drone_collection
from flock_controller.mechanics.commands import gen_Command, issue_command
from flock_controller.mechanics.location import find_nearest_drone
from flock_controller.mechanics.messages import get_message_collection, get_message, delete_message

global LOOP_TIME

# Keeping loop time more than drone to prevent requests before update is complete
LOOP_TIME = 17


def is_confirming(drone):
    """Check if the drone is in confirmation state."""
    return drone["DroneState"]["Status"] == "Confirming"


def is_active(drone):
    """Check if the drone is in confirmation state."""
    return drone["DroneState"]["Status"] == "Active"


def handle_anomaly(anomaly, drone_collection):
    """Handle the anomaly by sending a drone to check it out."""
    drone = find_nearest_drone(drone_collection, anomaly)
    if drone is not None:
        anomaly["Status"] = "Confirming"
        update_anomaly(anomaly["AnomalyID"], anomaly)
        send_anomaly(anomaly, drone["DroneID"])
        print("Anomaly handled successfully.")
    return None


def find_non_confirmed_and_negative_anomalies(anomaly_collection):
    """ Find the anomalies with status 'To be Confirmed' or "Negative"."""
    non_confirmd_anomalies, negative_anomalies = list(), list()
    for anomaly in anomaly_collection:
        anomaly_id = None
        regex = r'/(.*)/(\d*)'
        matchObj = re.match(regex, anomaly["@id"])
        if matchObj:
            anomaly_id = matchObj.group(2)
        if anomaly_id is not None:
            anomaly = get_anomaly(anomaly_id)
            if anomaly["Status"] == "To be Confirmed":
                non_confirmd_anomalies.append(anomaly)
            elif anomaly["Status"] == "Negative":
                negative_anomalies.append(anomaly)
    return non_confirmd_anomalies, negative_anomalies


def parse_message(message_string):
    """ Parse a given message string.
    Messages will be in format 'Set Drone <DroneID> <Property> <Value>'.
    DroneID is the drone identifier assigned by the central controller.
    Property can be Direction, Speed or Status and values can be anything
    supported by that respective Property."""

    message_items = message_string.split(" ")
    try:
        drone_id = message_items[message_items.index("Drone") + 1]
        prop = message_items[message_items.index(drone_id) + 1].title()
        value = message_items[message_items.index(prop) + 1]

        return (drone_id, prop, value)
    except Exception as e:
        print(e)
        return None

def validate_message_prop_value(prop, value):
    """Check if prop and value is valid."""

    if prop not in ["Direction", "Speed", "Status"]:
        return False

    if prop == "Direction":
        if value not in ["E", "W", "N", "S"]:
            return False

    if prop == "Speed":
        if not value.isdigit():
            return False

    if prop == "Status":
        if value not in ["Off", "Active"]:
            return False

    return True

def generate_command(drone_id, prop, value):
    """Generate a command object given a property and value."""
    state = {
        prop : value
    }
    command = gen_Command(drone_id, state)
    return command


def handle_messages():
    """Handle messages in the MessageCollection."""
    message_collection = get_message_collection()

    for message in message_collection:
        regex = r'/(.*)/(\d*)'
        matchObj = re.match(regex, message["@id"])
        if matchObj:
            message_id = matchObj.group(2)
            message_details = get_message(message_id)

            ## parse message
            parsed_message = parse_message(message_details["MessageString"])

            if parsed_message is not None:
                drone_id, prop, value = parsed_message
                if not validate_message_prop_value(prop, value):
                    delete_message(message_id)
                else:
                    command = generate_command(drone_id, prop, value)
                    RES, NAMESPACE = find_res(drone_id)
                    if RES is not None and NAMESPACE is not None:
                        issue_command(RES, NAMESPACE, command)
            else:
                ## If error in parsing message then delete message.
                delete_message(message_id)

    threading.Timer(3, handle_messages).start()




def main():
    """15 second time loop for drone."""
    print("Simulation")

    anomaly_collection = get_anomaly_collection()
    drone_collection = get_drone_collection()

    non_confirmed_anomalies, negative_anomalies = find_non_confirmed_and_negative_anomalies(
        anomaly_collection)
    print(non_confirmed_anomalies)
    # Handle non_confirmed_anomalies
    for anomaly in non_confirmed_anomalies:
        handle_anomaly(anomaly, drone_collection)

    # Delete Negative anomalies
    for anomaly in negative_anomalies:
        delete_anomaly(anomaly["AnomalyID"])

    threading.Timer(LOOP_TIME, main).start()


if __name__ == "__main__":
    main()
    ## To be implemented
    handle_messages()
