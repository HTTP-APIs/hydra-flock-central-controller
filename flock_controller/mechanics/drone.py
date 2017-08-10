"""Drone operations."""
import json
import re
import requests
# from hydra import Resource, SCHEMA
from flock_controller.mechanics.main import CENTRAL_SERVER, RES_CS, IRI_CS


def get_drone_collection():
    """Get the collection of drones from the server."""
    get_drone_collection_ = RES_CS.find_suitable_operation(None, None, CENTRAL_SERVER.DroneCollection)
    resp, body = get_drone_collection_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    body = json.loads(body.decode('utf-8'))

    body.pop("@context")
    body.pop("@type")

    drone_list = list()
    for drone in body["members"]:
        regex = r'/(.*)/(\d)'
        matchObj = re.match(regex, drone["@id"])
        if matchObj:
            drone = get_drone(matchObj.group(2))
            drone_list.append(drone)
    return drone_list


# def get_drone(id_):
#     """Get the drone from the server given the drone ID."""
#     IRI = IRI_CS + "/DroneCollection/" + str(id_)
#     RES = Resource.from_iri(IRI)
#     get_drone_ = RES.find_suitable_operation(SCHEMA.FindAction, None, CENTRAL_SERVER.Drone)
#     resp, body = get_drone_()
#     assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
#     body = json.loads(body.decode('utf-8'))
#
#     body.pop("@context")
#     body.pop("@type")
#     return body

def get_drone(id_):
    """Get the anomaly from central server."""
    try:
        RES = IRI_CS + "/DroneCollection/" + str(id_)
        response = requests.get(RES)

        assert response.status_code in [201, 200]

        drone = response.json()
        drone.pop("@context", None)
        drone.pop("@id", None)
        return drone

    except (ConnectionRefusedError, ConnectionError):
        raise ConnectionRefusedError("Connection Refused! Please check the drone server.")


if __name__ == "__main__":
    get_drone(2)
