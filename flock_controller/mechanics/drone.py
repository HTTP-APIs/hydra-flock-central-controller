"""Drone operations."""
import json
import re
import requests
from hydra import Resource, SCHEMA
from flock_controller.mechanics.main import CENTRAL_SERVER, RES_CS, IRI_CS


def get_drone_collection():
    """Get the collection of drones from the server."""
    try:
        get_drone_collection_ = RES_CS.find_suitable_operation(
            None, None, CENTRAL_SERVER.DroneCollection)
        resp, body = get_drone_collection_()
        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
        body = json.loads(body.decode('utf-8'))

        return body["members"]
    except Exception as e:
        print(e)
        return None


def gen_drone_list_from_collection(drone_collection):
    """Return a drone list with drone details from a drone collection."""
    drone_list = list()
    for drone in drone_collection:
        drone_id = drone["@id"].split("/")[-1]
        drone_details = get_drone(drone_id)
        drone_list.append(drone_details)
    return drone_list


def get_drone(id_):
    """Get the drone from the server given the drone ID."""
    try:
        IRI = IRI_CS + "/DroneCollection/" + str(id_)
        RES = Resource.from_iri(IRI)
        get_drone_ = RES.find_suitable_operation(
            output_type=CENTRAL_SERVER.Drone)
        resp, body = get_drone_()
        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
        body = json.loads(body.decode('utf-8'))

        body.pop("@context")
        body.pop("@type")
        return body

    except Exception as e:
        print(e)
        return None
