"""Handle main configuration for the Central server."""
import json
import re
from hydra import Resource
from rdflib import Namespace
from flock_controller.settings import CENTRAL_SERVER_NAMESPACE
from flock_controller.settings import DRONE1_NAMESPACE, DRONE2_NAMESPACE, DRONE3_NAMESPACE, DRONE4_NAMESPACE
from flock_controller.settings import IRI_CS, IRI_DRONE1, IRI_DRONE2, IRI_DRONE3, IRI_DRONE4


global CENTRAL_SERVER, DRONE1, DRONE2, DRONE3, DRONE4
CENTRAL_SERVER = Namespace(CENTRAL_SERVER_NAMESPACE)
# print(CENTRAL_SERVER)
DRONE1 = Namespace(DRONE1_NAMESPACE)
DRONE2 = Namespace(DRONE2_NAMESPACE)
DRONE3 = Namespace(DRONE3_NAMESPACE)
DRONE4 = Namespace(DRONE4_NAMESPACE)
DRONES = [DRONE1, DRONE2, DRONE2, DRONE4]
# print(DRONE1)

global RES_CS, RES_DRONE1, RES_DRONE2, RES_DRONE3, RES_DRONE4
RES_CS = Resource.from_iri(IRI_CS)
RES_DRONE1 = Resource.from_iri(IRI_DRONE1)
RES_DRONE2 = Resource.from_iri(IRI_DRONE2)
RES_DRONE3 = Resource.from_iri(IRI_DRONE3)
RES_DRONE4 = Resource.from_iri(IRI_DRONE4)
RES_DRONES = [RES_DRONE1, RES_DRONE2, RES_DRONE3, RES_DRONE4]


def gen_State(drone_id, battery, direction, position, sensor_status, speed):
    """Generate a State objects."""
    state = {
        "@type": "State",
        "DroneID": drone_id,
        "Battery": battery,
        "Direction": direction,
        "Position": position,
        "Status": sensor_status,
        "Speed": speed,
    }
    return state


# Some general Functions
def ordered(obj):
    """Sort json dicts and lists within."""
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def find_res(id_):
    """Find the resource for the drone, given the drone ID."""
    for i in range(1, 5):
        get_drone_ = RES_DRONES[i].find_suitable_operation(None, None, DRONES[i].Drone)
        resp, body = get_drone_()
        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
        body = json.loads(body.decode('utf-8'))
        regex = r'/(.*)/(\d)'
        matchObj = re.match(regex, body["@id"])
        if matchObj:
            if id_ == matchObj.group(2):
                return RES_DRONES[i], DRONES[i]
    return None
