"""Operations to update Area."""
from haversine import haversine
from flock_controller.mechanics.main import CENTRAL_SERVER, RES_CS
from flock_controller.mechanics.drone import gen_drone_list_from_collection
from hydra import SCHEMA, Resource


def gen_Location(coordinate_str):
    """Generate a Location object."""
    Area = {
        "@type": "Location",
        "Location": coordinate_str
    }
    return Area


def update_location(location):
    """Update the area of interest on central server."""
    update_location_ = RES_CS.find_suitable_operation(
                   operation_type=SCHEMA.UpdateAction,
                   input_type=CENTRAL_SERVER.Location)
    resp, body = update_location_(location)
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    return Resource.from_iri(resp['location'])


def add_location(location):
    """Update the area of interest on central server."""
    add_location_ = RES_CS.find_suitable_operation(
                   operation_type=SCHEMA.AddAction,
                   input_type=CENTRAL_SERVER.Location)
    resp, body = add_location_(location)
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    return Resource.from_iri(resp['location'])


def find_nearest_drone(drone_collection, anomaly):
    """Find the drone closest to the anomaly."""
    min_dist = 10000000000000
    closest_drone = None
    drone_list = gen_drone_list_from_collection(drone_collection)
    for drone in drone_list:
        if drone["DroneState"]["Status"] != "Confirming":
            if str(drone["DroneID"]) != str(anomaly["DroneID"]):
                drone_location = tuple([float(x) for x in drone["DroneState"]["Position"].split(',')])
                anomaly_location = tuple([float(x) for x in anomaly["Location"].split(',')])
                dist = haversine(drone_location, anomaly_location)
                if dist < min_dist:
                    min_dist = dist
                    closest_drone = drone
    return closest_drone


def get_direction(source, destination):
    """Find the direction drone needs to move to get from src to dest."""
    lat_diff = abs(source[0] - destination[0])
    long_diff = abs(source[1] - destination[1])
    if lat_diff > long_diff:
        if source[0] > destination[0]:
            return "S"
        else:
            return "N"
    else:
        if source[1] > destination[1]:
            return "W"
        else:
            return "E"


if __name__ == "__main__":
    # Initialise central server location at 0,0
    location = gen_Location("0.856901647439813,14.08447265625")
    print(location)
    print(add_location(location))
