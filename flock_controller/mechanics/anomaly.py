"""Script to handle all operations related to anomalies."""
import json
import re
from hydra import SCHEMA, Resource
from flock_drone.mechanics.main import RES_CS, CENTRAL_SERVER, IRI_CS
from flock_drone.mechanics.logs import (send_http_api_log, gen_HttpApiLog,
                                        send_dronelog, gen_DroneLog)


def get_new_state(anomaly, drone):
    """Get the new state of the drone to move towards the anomaly."""
    pass


def gen_Anomaly(location, id_):
    """Generate an anomaly object."""
    anomaly = {
        "@type": "Anomaly",
        "Location": location,
        "DroneID": id_
    }

    return anomaly


def get_anomaly(id_):
    """Get the anomaly from drone server."""
    try:
        RES = Resource(IRI_CS + "/DroneCollection/" + str(id_))
        get_anomaly_ = RES.find_suitable_operation(None, None, CENTRAL_SERVER.Anomaly)
        resp, body = get_anomaly_()
        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

        anomaly = json.loads(body.decode('utf-8'))
        anomaly.pop("@context", None)
        anomaly.pop("@id", None)
        return anomaly
    except ConnectionRefusedError:
        raise ConnectionRefusedError("Connection Refused! Please check the drone server.")


def get_anomaly_collection():
    """Get the anomaly from drone server."""
    try:
        get_anomaly_collection_ = RES_CS.find_suitable_operation(
            operation_type=None, input_type=None, output_type=CENTRAL_SERVER.AnomalyCollection)
        resp, body = get_anomaly_collection_()
        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

        anomalies = json.loads(body.decode('utf-8'))
        anomalies.pop("@context", None)
        anomalies.pop("@id", None)

        anomaly_list = list()
        for anomaly in anomalies["members"]:
            regex = r'/(.*)/(\d)'
            matchObj = re.match(regex, anomaly["@id"])
            if matchObj:
                anomaly = get_anomaly(matchObj.group(2))
                anomaly_list.append(anomaly)
        return anomaly_list

    except ConnectionRefusedError:
        raise ConnectionRefusedError("Connection Refused! Please check the drone server.")


def send_anomaly(anomaly, drone_identifier):
    """Send the drone current datastream to the central server."""
    post_anomaly = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.Anomaly)
    resp, body = post_anomaly(anomaly)

    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    print("Anomaly added successfully.")

    http_api_log = gen_HttpApiLog("Drone %s" % (str(drone_identifier)), "PUT Anomaly", "Controller")
    send_http_api_log(http_api_log)

    dronelog = gen_DroneLog("Drone %s" % (str(drone_identifier),),
                            "detected anomaly at %s" % (str(anomaly["Location"])))
    send_dronelog(dronelog)
