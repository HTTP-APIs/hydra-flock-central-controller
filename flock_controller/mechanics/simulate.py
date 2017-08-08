"""Main control loop for drone."""
import threading
import random
import re
from flock_drone.mechanics.main import (get_drone, update_drone,
                                        get_controller_location,
                                        update_drone_at_controller)

from flock_drone.mechanics.logs import (send_dronelog, send_http_api_log,
                                        gen_DroneLog, gen_HttpApiLog)

from flock_drone.mechanics.datastream import gen_Datastream, update_datastream, send_datastream
from flock_drone.mechanics.anomaly import gen_Anomaly, send_anomaly, get_anomaly, get_new_state
from flock_drone.mechanics.distance import get_new_coordinates, gen_square_path, gen_drone_pos_limits
from flock_drone.mechanics.commands import get_command_collection, get_command, delete_commands

# Drone main Loop time settings
global LOOP_TIME, ITERATOR
LOOP_TIME = 15

CONTROLLER_LOC = tuple(float(x) for x in get_controller_location().split(","))

DRONE_BOUNDS = gen_drone_pos_limits(gen_square_path(CONTROLLER_LOC, 10))

ITERATOR = 0


def handle_drone_commands(drone):
    """Handle the commands on the drone server and update drone accordingly."""
    # Using the latest command, not following previously stored ones, server will ensure order
    commands = get_command_collection()["members"]
    command_ids = [x["@id"] for x in commands]
    temp_list = list()
    for id_ in command_ids:
        regex = r'/(.*)/(\d)'
        matchObj = re.match(regex, id_)
        if matchObj:
            temp_list.append(matchObj.group(2))
    temp_list.sort()

    latest_command = get_command(temp_list[-1])
    # Execute the latest command
    drone = execute_command(latest_command, drone)
    # Delete after execution
    delete_commands(temp_list)

    return drone


def execute_command(command, drone):
    """Execute the command on the drone."""
    if command["DroneID"] == drone["DroneID"]:
        drone["DroneState"] = command["State"]

    return drone


# Battery related functions
def discharge_drone_battery(drone):
    """Handle drone battery discharging."""
    battery_level = drone["DroneState"]["Battery"]
    drone_identifier = drone["DroneID"]
    if(int(battery_level) > 3):
        drone["DroneState"]["Battery"] = int(drone["DroneState"]["Battery"])-1
    else:
        # Battery level critical change drone status to OFF
        drone["DroneState"]["Status"] = "Off"

    if int(battery_level) == 20:

        dronelog = gen_DroneLog("Drone %s" % (str(drone_identifier),), "battery Low %s" % (str(drone["DroneState"]["Battery"])))
        send_dronelog(dronelog)

        http_api_log = gen_HttpApiLog("Drone %s" % (str(drone_identifier)), "PUT DroneLog", "Controller")
        send_http_api_log(http_api_log)

    elif int(battery_level) == 4:

        dronelog = gen_DroneLog("Drone %s" % (str(drone_identifier)), "Battery level critical, will shutdown soon!")
        send_dronelog(dronelog)

        http_api_log = gen_HttpApiLog("Drone %s" % (str(drone_identifier)), "PUT DroneLog", "Controller")
        send_http_api_log(http_api_log)

    return drone


def charge_drone_battery(drone):
    """Handle the drone battery charging operration."""
    battery_level = drone["DroneState"]["Battery"]
    if int(battery_level) < 95:
        # Increase battery level
        drone["DroneState"]["Battery"] = int(battery_level) + 5
    else:
        # If battery >= 95 set battery level to 100%
        drone["DroneState"]["Battery"] = 100
    return drone


def is_drone_charging(drone):
    """Check if the drone status is charging."""
    return drone["DroneState"]["Status"] == "Charging"


def drone_is_not_off(drone):
    """Check if drone status is not off."""
    return drone["DroneState"]["Status"] != "Off"


def handle_drone_battery(drone):
    """Handle the drone battery status."""
    if drone_is_not_off(drone):
        if is_drone_charging(drone):
            drone = charge_drone_battery(drone)
        else:
            drone = discharge_drone_battery(drone)
    return drone


# Distance related functions
def is_valid_location(location, bounds):
    """Check if location is in drone bounds."""
    if min(bounds[0]) <= location[0] <= max(bounds[0]):
        if min(bounds[1]) <= location[1] <= max(bounds[1]):
            return True
    return False


def is_confirming(drone):
    """Check if the drone is in confirmation state."""
    return drone["DroneState"]["Status"] == "Confirming"


def get_random_direction_for_drone():
    """Return a random direction for drone."""
    return random.choice(["N", "S", "E", "W"])


def handle_invalid_pos(drone, distance_travelled):
    """Handle invalid position update for drone."""
    direction = get_random_direction_for_drone()
    drone["DroneState"]["Direction"] = direction

    drone_position = tuple(float(a) for a in drone["DroneState"]["Position"].split(","))
    new_drone_position = get_new_coordinates(drone_position, distance_travelled, direction)
    if is_valid_location(new_drone_position, DRONE_BOUNDS):
        drone["DroneState"]["Position"] = ",".join(map(str, new_drone_position))
        return drone
    else:
        return handle_invalid_pos(drone, distance_travelled)


def calculate_dis_travelled(speed, time):
    """Calculate the distance travelled(in Km) in a give amount of time(s)."""
    return (speed*time)/3600.0


def update_drone_position(drone, distance_travelled, direction):
    """Update the drone position given the distance travelled and direction of travel."""
    drone_position = tuple(float(a) for a in drone["DroneState"]["Position"].split(","))
    new_drone_position = get_new_coordinates(drone_position, distance_travelled, direction)
    if is_valid_location(new_drone_position, DRONE_BOUNDS):
        drone["DroneState"]["Position"] = ",".join(map(str, new_drone_position))
    else:
        drone = handle_invalid_pos(drone, distance_travelled)
    return drone


def handle_drone_position(drone):
    """Handle the drone position changes."""
    drone_speed = float(drone["DroneState"]["Speed"])
    distance_travelled = calculate_dis_travelled(drone_speed, LOOP_TIME)
    drone_direction = str(drone["DroneState"]["Direction"])
    drone_identifier = drone["DroneID"]
    new_drone = update_drone_position(drone, distance_travelled, drone_direction)

    if(new_drone["DroneState"]["Direction"] != drone_direction):

        dronelog = gen_DroneLog("Drone %s" % (str(drone_identifier),),
                                "changed direction to %s" % (str(new_drone["DroneState"]["Direction"])))
        send_dronelog(dronelog)

        http_api_log = gen_HttpApiLog("Drone %s" % (str(drone_identifier)),
                                      "PUT DroneLog", "Controller")
        send_http_api_log(http_api_log)

    return new_drone


def gen_normal_sensor_data():
    """Generate normal sensor data for drone datastream."""
    normal_range = range(25, 40)
    return random.choice(normal_range)


def gen_abnormal_sensor_data():
    """Generate abnormal sensor data for drone datastream."""
    abnormal_range = range(45, 60)
    return random.choice(abnormal_range)


def gen_random_anomaly(drone):
    """Generate an anomaly at random."""
    global ITERATOR
    ITERATOR += 1
    # 1/3 chance of anomaly every ten iterations
    if ITERATOR % 10 == 0:
        ITERATOR = 0
        option = random.choice([False, True, False])
        if option:
            anomaly = gen_Anomaly(drone["DroneState"]["Position"])
            return anomaly
    return None


def handle_anomaly(anomaly):
    """Handle the anomaly by sending a drone to check it out."""
    drones = get_drone_collection()
    drone = find_nearest_drone(drones, anomaly)
    issue_anomaly(drone, anomaly)



def main():
    """15 second time loop for drone."""
    anomalies = get_anomaly_collection()
    for anomaly in anomalies:
        handle_anomaly(anomaly)


if __name__ == "__main__":
    main()
