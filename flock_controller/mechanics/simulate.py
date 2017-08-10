"""Main control loop for drone."""
import threading
from flock_controller.mechanics.main import find_res

from flock_controller.mechanics.anomaly import send_anomaly, get_anomaly_collection
from flock_controller.mechanics.drone import get_drone_collection
from flock_controller.mechanics.commands import confirm_anomaly, issue_command
from flock_controller.mechanics.location import find_nearest_drone

global LOOP_TIME
LOOP_TIME = 20      # Keeping loop time more than drone to prevent requests before update is complete


def is_confirming(drone):
    """Check if the drone is in confirmation state."""
    return drone["DroneState"]["Status"] == "Confirming"


def handle_anomaly(anomaly):
    """Handle the anomaly by sending a drone to check it out."""
    drones = get_drone_collection()
    drone = find_nearest_drone(drones, anomaly)
    if drone is not None:
        send_anomaly(anomaly, drone["DroneID"])
        drone_command = confirm_anomaly(drone)
        return (drone_command, drone)
    return None


def main():
    """15 second time loop for drone."""
    print("Simulation")
    anomalies = get_anomaly_collection()

    for anomaly in anomalies:
        print("Handling anomaly")
        response = handle_anomaly(anomaly)
        if response is not None:
            print("Assigning drone")
            command, drone = response
            RES, NAMESPACE = find_res(drone)
            print("Issueing command")
            issue_command(RES, NAMESPACE, drone)

    # call main() again in LOOP_TIME
    threading.Timer(LOOP_TIME, main).start()


if __name__ == "__main__":
    main()
