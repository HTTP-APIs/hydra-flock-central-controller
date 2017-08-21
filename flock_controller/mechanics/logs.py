"""Operations for managing logs."""
from hydra import Resource, SCHEMA
from flock_controller.mechanics.main import CENTRAL_SERVER, RES_CS


def gen_ControllerLog(log_string, drone_id):
    """Generate a Controller log object from log string."""
    controllerlog = {
        "@type": "ControllerLog",
        "LogString": log_string,
        "DroneID": drone_id,
    }
    return controllerlog


def send_controllerlog(controllerlog):
    """Post the controller log to the central server."""
    try:
        post_controllerlog = RES_CS.find_suitable_operation(
            SCHEMA.AddAction, CENTRAL_SERVER.ControllerLog)
        resp, body = post_controllerlog(controllerlog)

        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
        new_controllerlog = Resource.from_iri(resp['location'])
        print("Controller Log successfully.")
        return new_controllerlog
    except Exception as e:
        print(e)
        return None

def gen_HttpApiLog(source, action, target):
    """Generate a Http Api Log object from action and target."""
    httpapilog = {
        "@type": "HttpApiLog",
        "Subject": source,
        "Predicate": action,
        "Object": target
    }
    return httpapilog


def send_http_api_log(http_api_log):
    """Post the drone http Api Log to the central server."""
    try:
        post_http_api_log = RES_CS.find_suitable_operation(
            SCHEMA.AddAction, CENTRAL_SERVER.HttpApiLog)
        resp, body = post_http_api_log(http_api_log)

        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
        new_http_api_log = Resource.from_iri(resp['location'])
        print("Http Api Log posted successfully.")
        return new_http_api_log
    except Exception as e:
        print(e)
        return None
