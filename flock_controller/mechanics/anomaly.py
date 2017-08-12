"""Script to handle all operations related to anomalies."""
import json
import re
import haversine
import requests
from hydra import SCHEMA, Resource
from flock_controller.mechanics.main import RES_CS, CENTRAL_SERVER, IRI_CS, find_res
from flock_controller.mechanics.logs import send_http_api_log, gen_HttpApiLog, gen_ControllerLog, send_controllerlog
from flock_controller.mechanics.location import get_direction


def gen_Anomaly(location, id_):
    """Generate an anomaly object."""
    anomaly = {
        "@type": "Anomaly",
        "Location": location,
        "DroneID": id_,
        "Status": "To be Confirmed",
        "AnomalyID": "-1"
    }

    return anomaly


def get_anomaly(id_):
    """Get the anomaly with id=id_ from central server."""
    try:
        RES = Resource.from_iri(IRI_CS + "/AnomalyCollection/" + str(id_))
        get_anomaly_ = RES.find_suitable_operation(None, None, CENTRAL_SERVER.Anomaly)
        resp, body = get_anomaly_()
        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

        anomaly = json.loads(body.decode('utf-8'))
        anomaly.pop("@context", None)
        anomaly.pop("@id", None)
        return anomaly
    except ConnectionRefusedError:
        raise ConnectionRefusedError("Connection Refused! Please check the drone server.")


def update_anomaly(id_, anomaly):
    """Update the anomaly at central controller."""
    try:
        RES = Resource.from_iri(IRI_CS + "/AnomalyCollection/" + str(id_))
        update_anomaly_ = RES.find_suitable_operation(operation_type=SCHEMA.UpdateAction, input_type=CENTRAL_SERVER.Anomaly)
        resp, body = update_anomaly_(anomaly)
        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

        print("Anomaly Updated successfully.")
        return Resource.from_iri(resp['location'])
    except ConnectionRefusedError:
        raise ConnectionRefusedError("Connection Refused! Please check the drone server.")


def delete_anomaly(id_):
    """Delete a anomaly from the collection given the anomaly id."""
    try:
        i = Resource.from_iri(IRI_CS + "/AnomalyCollection/" + str(id_))
        # name = i.value(SCHEMA.name)
        resp, _ = i.find_suitable_operation(SCHEMA.DeleteAction)()
        print("RESP, RESP")
        if resp.status // 100 != 2:
            return "error deleting <%s>" % i.identifier
        else:
            return "deleted <%s>" % i.identifier
    except Exception as e:
        print(e)
        return {404: "Resource with Id %s not found!" % (id_,)}


def get_anomaly_collection():
    """Get the anomaly collection from central server."""
    try:
        get_anomaly_collection_ = RES_CS.find_suitable_operation(
            operation_type=None, input_type=None, output_type=CENTRAL_SERVER.AnomalyCollection)
        resp, body = get_anomaly_collection_()
        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

        anomalies = json.loads(body.decode('utf-8'))
        anomalies.pop("@context", None)
        anomalies.pop("@id", None)
        return anomalies["members"]

    except ConnectionRefusedError:
        raise ConnectionRefusedError("Connection Refused! Please check the drone server.")


def send_anomaly(anomaly, drone_identifier):
    """Send the anomaly to the respective drone."""
    RES, NAMESPACE = find_res(drone_identifier)
    print(RES, NAMESPACE)
    post_anomaly = RES.find_suitable_operation(operation_type=SCHEMA.UpdateAction, input_type=NAMESPACE.Anomaly)
    resp, body = post_anomaly(anomaly)

    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    print("Anomaly sent successfully.")

    http_api_log = gen_HttpApiLog("Central Controller ", "PUT Anomaly", "Drone %s" % (str(drone_identifier)))
    send_http_api_log(http_api_log)

    controllerlog = gen_ControllerLog("Central Controller assigned Anomaly %s to" %(str(anomaly["AnomalyID"])), "Drone %s" %(str(drone_identifier)))

#
# def get_new_state(anomaly, drone):
#     """Create the new drone state based on the anomaly."""
#     drone_position = tuple([float(x) for x in drone["DroneState"]["Position"].split(',')])
#     anomaly_position = tuple([float(x) for x in anomaly["Location"].split(',')])
#
#     if haversine(drone_position, anomaly_position) < 10:
#         drone["DroneState"]["State"] = "Active"
#         return drone, "ReadData"
#
#     direction = get_direction(source=drone_position, destination=anomaly_position)
#     drone["DroneState"]["Direction"] = direction
#     return drone, None
#

if __name__ == "__main__":
    # print(get_anomaly_collection())
    # anomaly = get_anomaly(24)
    # anomaly["DroneID"] = "24"
    # print(anomaly)
    # update_anomaly(24, anomaly)
    #
    # anomaly_collection = get_anomaly_collection()
    # print(anomaly_collection)
    #
    # print(send_anomaly(anomaly, 10))
    print(delete_anomaly(24))
