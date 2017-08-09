"""Operations for managing logs."""
from hydra import Resource, SCHEMA
from flock_controller.mechanics.main import CENTRAL_SERVER, RES_CS


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
    post_http_api_log = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.HttpApiLog)
    resp, body = post_http_api_log(http_api_log)

    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    new_http_api_log = Resource.from_iri(resp['location'])
    print("Http Api Log posted successfully.")
    return new_http_api_log
