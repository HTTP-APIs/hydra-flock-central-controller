"""Operations for managing data readings."""
# from hydra import Resource, SCHEMA
from flock_controller.mechanics.main import DRONE1, DRONE2, DRONE3, DRONE4, CENTRAL_SERVER
from flock_controller.mechanics.main import RES_DRONE1, RES_DRONE2, RES_DRONE3, RES_DRONE4, RES_CS
import pdb
# from flock_controller.mechanics.main import gen_Command, gen_State
import json


def get_data_collection():
    """Get command collection from the central server."""
    get_data_collection_ = RES_CS.find_suitable_operation(None, None, CENTRAL_SERVER.DatastreamCollection)
    resp, body = get_data_collection_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    body = json.loads(body.decode('utf-8'))
    return body


def find_anamoly(data_collection):
    """Find the anomaly in the given data."""
    pass


if __name__ == "__main__":
    data = get_data_collection()
    pdb.set_trace()
