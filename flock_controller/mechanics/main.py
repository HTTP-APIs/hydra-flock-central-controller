"""Handle main configuration for the Central server."""
from hydra import Resource
from rdflib import Namespace
from flock_controller.settings import CENTRAL_SERVER_NAMESPACE, DRONE1_NAMESPACE
from flock_controller.settings import DRONE1_URL, CENTRAL_SERVER_URL
from flock_controller.settings import IRI_CS, IRI_DRONE1


global CENTRAL_SERVER, DRONE1, DRONE_URL
CENTRAL_SERVER = Namespace(CENTRAL_SERVER_NAMESPACE)
print(CENTRAL_SERVER)
DRONE1 = Namespace(DRONE1_NAMESPACE)
# print(DRONE1)

global RES_CS, RES_DRONE
RES_CS = Resource.from_iri(IRI_CS)
RES_DRONE1 = Resource.from_iri(IRI_DRONE1)


# Methods related to Area
def gen_Area(top_left, bottom_right):
    """Generate a Area object."""
    Area = {
        "@type": "Area",
        "TopLeft": top_left,
        "BottomRight": bottom_right
    }
    return Area
# area = gen_Area("0,0", "5,5")


# Methods related to Messages
def gen_Message(message):
    """Create a new Message."""
    message = {
        "@type": "Message",
        "MessageString": message,
    }
    return message


# Methods related to commands
def gen_State(drone_id, battery, direction, position, sensor_status, speed):
    """Generate a State objects."""
    state = {
        "@type": "State",
        "DroneID": drone_id,
        "Battery": battery,
        "Direction": direction,
        "Position": position,
        "SensorStatus": sensor_status,
        "Speed": speed,
    }
    return state
# state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
# print(state)


def gen_Command(state):
    """Generate a Command object."""
    command = {
        "@type": "Command",
        "State": state
    }
    return command
