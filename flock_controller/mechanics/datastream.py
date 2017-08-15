"""Operations for managing data readings."""
# from hydra import Resource, SCHEMA
from flock_controller.mechanics.main import CENTRAL_SERVER, RES_CS
import pdb
import json


def get_data_collection():
    """Get command collection from the central server."""
    get_data_collection_ = RES_CS.find_suitable_operation(
        None, None, CENTRAL_SERVER.DatastreamCollection)
    resp, body = get_data_collection_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    body = json.loads(body.decode('utf-8'))
    return body["members"]


if __name__ == "__main__":
    data = get_data_collection()
    # pdb.set_trace()
