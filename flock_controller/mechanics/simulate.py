"""Main control loop for drone."""
import threading
from flock_controller.mechanics.main import find_res
import re
from flock_controller.mechanics.anomaly import send_anomaly, get_anomaly_collection, get_anomaly
from flock_controller.mechanics.anomaly import delete_anomaly, update_anomaly
from flock_controller.mechanics.drone import get_drone_collection
from flock_controller.mechanics.commands import confirm_anomaly, issue_command
from flock_controller.mechanics.location import find_nearest_drone

global LOOP_TIME
LOOP_TIME = 20      # Keeping loop time more than drone to prevent requests before update is complete


def is_confirming(drone):
    """Check if the drone is in confirmation state."""
    return drone["DroneState"]["Status"] == "Confirming"


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



def main():
    """15 second time loop for drone."""
    print("Simulation")
    anomaly_collection = get_anomaly_collection()
    drone_collection = get_drone_collection()

    non_confirmed_anomalies, negative_anomalies = find_non_confirmed_and_negative_anomalies(anomaly_collection)

    ## Handle non_confirmed_anomalies
    for anomaly in non_confirmed_anomalies:
        handle_anomaly(anomaly, drone_collection)

    ## Delete Negative anomalies
    for anomaly in negative_anomalies:
        delete_anomaly(anomaly["AnomalyID"])



    threading.Timer(LOOP_TIME, main).start()


if __name__ == "__main__":
    main()
