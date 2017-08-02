"""Operations for managing logs."""
from hydra import Resource, SCHEMA
from mechanics.main import CENTRAL_SERVER
from mechanics.main import RES_CS
from mechanics.main import gen_Log
import json


def get_logs_collection():
    """Get logs collection from the central server."""
    get_logs_collection_ = RES_CS.find_suitable_operation(None, None, CENTRAL_SERVER.LogEntryCollection)
    resp, body = get_logs_collection_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    body = json.loads(body.decode('utf-8'))
    return body


def create_log(log):
    """Add a log object entity to the central server."""
    create_log_ = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.LogEntry)
    resp, body = create_log_(log)

    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    new_log = Resource.from_iri(resp['location'])
    print("Log created successfully.")
    return new_log


if __name__ == "__main__":
    print(get_logs_collection())
    log = gen_Log("Log String 1")
    print(create_log(log))
