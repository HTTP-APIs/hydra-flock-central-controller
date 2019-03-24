"""API Doc generator for the server side API."""

from hydra_python_core.doc_writer import HydraDoc, HydraClass, HydraClassProp, HydraClassOp
import json
import os
from flock_controller.settings import HYDRUS_SERVER_URL


def doc_gen(API, BASE_URL):
    """Generate API Doc for server."""
    # Main API Doc
    api_doc = HydraDoc(API,
                       "API Doc for the server side API",
                       "API Documentation for the server side system",
                       API,
                       BASE_URL)

    # State Class
    state = HydraClass("State", "State", "Class for drone state objects")
    # Properties
    # Status include Active, Inactive, Off, Charging
    state.add_supported_prop(HydraClassProp(
        "http://auto.schema.org/speed", "Speed", False, False, True))
    state.add_supported_prop(HydraClassProp(
        "http://schema.org/geo", "Position", False, False, True))
    state.add_supported_prop(HydraClassProp(
        "http://schema.org/Property", "Direction", False, False, True))
    state.add_supported_prop(HydraClassProp(
        "http://schema.org/fuelCapacity", "Battery", False, False, True))
    state.add_supported_prop(HydraClassProp(
        "https://schema.org/status", "Status", False, False, True))
    state.add_supported_prop(HydraClassProp(
        "http://schema.org/identifier", "DroneID", False, False, True))

    # Drone Class
    drone = HydraClass("Drone", "Drone", "Class for a drone")
    # Properties
    drone.add_supported_prop(HydraClassProp(
        "vocab:State", "State", False, False, True))
    drone.add_supported_prop(HydraClassProp(
        "http://schema.org/name", "name", False, False, True))
    drone.add_supported_prop(HydraClassProp(
        "http://schema.org/model", "model", False, False, True))
    drone.add_supported_prop(HydraClassProp(
        "http://auto.schema.org/speed", "MaxSpeed", False, False, True))
    drone.add_supported_prop(HydraClassProp(
        "http://schema.org/device", "Sensor", False, False, True))
    # Operations
    # Drones will submit their state to the server at certain intervals or when some event happens
    drone.add_supported_op(HydraClassOp("SubmitDrone",
                                        "POST",
                                        "vocab:Drone",
                                        None,
                                        [{"statusCode": 200, "description": "Drone updated"}]))

    drone.add_supported_op(HydraClassOp("UpdateDrone",
                                        "PUT",
                                        "vocab:Drone",
                                        None,
                                        [{"statusCode": 200, "description": "Drone updated"}]))
    # Mechanics or GUI need to get the drone, it contains the state object of the drone already.
    drone.add_supported_op(HydraClassOp("GetDrone",
                                        "GET",
                                        None,
                                        "vocab:Drone",
                                        [{"statusCode": 404, "description": "Drone not found"},
                                         {"statusCode": 200, "description": "Drone Returned"}]))
    drone.add_supported_op(HydraClassOp("DeleteDrone",
                                        "DELETE",
                                        None,
                                        None,
                                        [{"statusCode": 404, "description": "Drone not found"},
                                         {"statusCode": 200, "description": "Drone successfully deleted."}]))

    # NOTE: Commands are stored in a collection. You may GET a command or you may DELETE it, there is not UPDATE.
    command = HydraClass("Command", "Command", "Class for drone commands")
    command.add_supported_prop(HydraClassProp(
        "http://schema.org/identifier", "DroneID", False, False, True))
    command.add_supported_prop(HydraClassProp(
        "vocab:State", "State", False, False, True))
    # Used by mechanics to get newly added commands
    command.add_supported_op(HydraClassOp("GetCommand",
                                          "GET",
                                          None,
                                          "vocab:Command",
                                          [{"statusCode": 404, "description": "Command not found"},
                                           {"statusCode": 200, "description": "Command Returned"}]))
    # Used by server to add new commands
    command.add_supported_op(HydraClassOp("AddCommand",
                                          "PUT",
                                          "vocab:Command",
                                          None,
                                          [{"statusCode": 201, "description": "Command added"}]))

    # Data is stored as a collection. Each data object can be read.
    # New data added to the collection
    datastream = HydraClass("Datastream", "Datastream",
                            "Class for a datastream entry")
    datastream.add_supported_prop(HydraClassProp(
        "http://schema.org/QuantitativeValue", "Temperature", False, False, True))
    datastream.add_supported_prop(HydraClassProp(
        "http://schema.org/identifier", "DroneID", False, False, True))
    datastream.add_supported_prop(HydraClassProp(
        "http://schema.org/geo", "Position", False, False, True))
    datastream.add_supported_op(HydraClassOp("ReadDatastream",
                                             "GET",
                                             None,
                                             "vocab:Datastream",
                                             [{"statusCode": 404, "description": "Data not found"},
                                              {"statusCode": 200, "description": "Data returned"}]))

    dronelog = HydraClass("DroneLog", "DroneLog",
                          "Class for a drone log entry")
    dronelog.add_supported_prop(HydraClassProp(
        "http://schema.org/identifier", "DroneID", False, False, True))
    dronelog.add_supported_prop(HydraClassProp(
        "http://schema.org/Text", "LogString", False, False, True))
    dronelog.add_supported_op(HydraClassOp("ReadDroneLog",
                                           "GET",
                                           None,
                                           "vocab:DroneLog",
                                           [{"statusCode": 404, "description": "DroneLog not found"},
                                            {"statusCode": 200, "description": "DroneLog returned"}]))

    controllerlog = HydraClass(
        "ControllerLog", "ControllerLog", "Class for a controller log entry")
    controllerlog.add_supported_prop(HydraClassProp(
        "http://schema.org/Text", "LogString", False, False, True))
    controllerlog.add_supported_prop(HydraClassProp(
        "http://schema.org/identifier", "DroneID", False, False, True))
    controllerlog.add_supported_op(HydraClassOp("ReadControllerLog",
                                                "GET",
                                                None,
                                                "vocab:ControllerLog",
                                                [{"statusCode": 404, "description": "ControllerLog not found"},
                                                 {"statusCode": 200, "description": "ControllerLog returned"}]))

    httpapilog = HydraClass("HttpApiLog", "HttpApiLog",
                            "Class for a http api log entry")
    httpapilog.add_supported_prop(HydraClassProp(
        "http://schema.org/identifier", "Subject", False, False, True))
    httpapilog.add_supported_prop(HydraClassProp(
        "http://schema.org/Action", "Predicate", False, False, True))
    httpapilog.add_supported_prop(HydraClassProp(
        "http://schema.org/identifier", "Object", False, False, True))
    httpapilog.add_supported_op(HydraClassOp("ReadHttpApiLog",
                                             "GET",
                                             None,
                                             "vocab:HttpApiLog",
                                             [{"statusCode": 404, "description": "HttpApiLog not found"},
                                              {"statusCode": 200, "description": "HttpApiLog returned"}]))

    # Single object representing the area of interest. No collections.
    location = HydraClass("Location", "Location",
                          "Class for location of the central controller.", endpoint=True)
    # Using two positions to have a bounding box
    location.add_supported_prop(HydraClassProp(
        "http://schema.org/geo", "Location", False, False, True))
    # Allowing updation of the area of interest
    location.add_supported_op(HydraClassOp("UpdateLocation",
                                           "POST",
                                           "vocab:Location",
                                           None,
                                           [{"statusCode": 200, "description": "Controller location updated successfully."}]))
    location.add_supported_op(HydraClassOp("AddLocation",
                                           "PUT",
                                           "vocab:Location",
                                           None,
                                           [{"statusCode": 200, "description": "Controller location added successfully."}]))
    location.add_supported_op(HydraClassOp("GetLocation",
                                           "GET",
                                           None,
                                           "vocab:Location",
                                           [{"statusCode": 404, "description": "Location of Controller not found."},
                                            {"statusCode": 200, "description": "Location of controller returned."}]))

    message = HydraClass("Message", "Message",
                         "Class for messages received by the GUI interface")
    message.add_supported_prop(HydraClassProp(
        "http://schema.org/Text", "MessageString", False, False, True))
    message.add_supported_op(HydraClassOp("GetMessage",
                                          "GET",
                                          None,
                                          "vocab:Message",
                                          [{"statusCode": 404, "description": "Message not found"},
                                           {"statusCode": 200, "description": "Message returned"}]))
    message.add_supported_op(HydraClassOp("DeleteMessage",
                                          "DELETE",
                                          None,
                                          None,
                                          [{"statusCode": 404, "description": "Message not found"},
                                           {"statusCode": 200, "description": "Message successfully deleted."}]))

    anomaly = HydraClass(
        "Anomaly", "Anomaly", "Class for Temperature anomalies that need to be confirmed")
    anomaly.add_supported_prop(HydraClassProp(
        "vocab:Location", "Location", False, False, True))
    anomaly.add_supported_prop(HydraClassProp(
        "http://schema.org/identifier", "DroneID", False, False, True))
    # Status of any anomaly can be ["Positive", "Negative", "Confirming", "To be confirmed"]
    anomaly.add_supported_prop(HydraClassProp(
        "http://schema.org/eventStatus", "Status", False, False, True))
    anomaly.add_supported_prop(HydraClassProp(
        "http://schema.org/identifier", "AnomalyID", False, False, True))

    anomaly.add_supported_op(HydraClassOp("GetAnomaly",
                                          "GET",
                                          None,
                                          "vocab:Anomaly",
                                          [{"statusCode": 404, "description": "Anomaly not found"},
                                           {"statusCode": 200, "description": "Anomaly returned"}]))
    anomaly.add_supported_op(HydraClassOp("AddAnomaly",
                                          "PUT",
                                          "vocab:Anomaly",
                                          None,
                                          [{"statusCode": 200, "description": "Anomaly added successfully."}]))
    anomaly.add_supported_op(HydraClassOp("UpdateAnomaly",
                                          "POST",
                                          "vocab:Anomaly",
                                          None,
                                          [{"statusCode": 201, "description": "Anomaly updated successfully."}]))
    anomaly.add_supported_op(HydraClassOp("DeleteAnomaly",
                                          "DELETE",
                                          None,
                                          None,
                                          [{"statusCode": 404, "description": "Anomaly not found"},
                                           {"statusCode": 200, "description": "Anomaly successfully deleted."}]))

    api_doc.add_supported_class(drone, collection=True)
    api_doc.add_supported_class(state, collection=False)
    api_doc.add_supported_class(datastream, collection=True)
    api_doc.add_supported_class(dronelog, collection=True)
    api_doc.add_supported_class(controllerlog, collection=True)
    api_doc.add_supported_class(httpapilog, collection=True)
    api_doc.add_supported_class(location, collection=False)
    api_doc.add_supported_class(command, collection=True)
    api_doc.add_supported_class(message, collection=True)
    api_doc.add_supported_class(anomaly, collection=True)

    api_doc.add_baseResource()
    api_doc.add_baseCollection()
    api_doc.gen_EntryPoint()
    return api_doc


if __name__ == "__main__":
    dump = json.dumps(
        doc_gen("api", HYDRUS_SERVER_URL).generate(), indent=4, sort_keys=True)
    doc = '''"""\nGenerated API Documentation for Server API using server_doc_gen.py."""\n\ndoc = %s''' % dump
    doc = doc + '\n'
    doc = doc.replace('true', '"true"')
    doc = doc.replace('false', '"false"')
    doc = doc.replace('null', '"null"')
    f = open(os.path.join(os.path.dirname(__file__), "doc.py"), "w")
    f.write(doc)
    f.close()
