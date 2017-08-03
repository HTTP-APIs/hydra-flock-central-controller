"""Operations to update Area."""
from flock_controller.mechanics.main import CENTRAL_SERVER
from flock_controller.mechanics.main import RES_CS
from flock_controller.mechanics.main import gen_Location
from hydra import SCHEMA, Resource


def update_location(location):
    """Update the area of interest on central server."""
    update_location_ = RES_CS.find_suitable_operation(
                   operation_type=SCHEMA.UpdateAction,
                   input_type=CENTRAL_SERVER.Location)
    resp, body = update_location_(location)
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    return Resource.from_iri(resp['location'])


if __name__ == "__main__":
    ## Initialise central server location at 0,0
    location = gen_Location("0.856901647439813,14.08447265625")
    print(location)

    print(update_location(location))
