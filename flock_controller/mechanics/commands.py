"""Operations for managing commands."""
from hydra import Resource, SCHEMA
from flock_controller.mechanics.main import CENTRAL_SERVER, RES_CS
import json


def gen_Command(drone_id, state):
    """Generate a Command object."""
    command = {
        "@type": "Command",
        "DroneID": drone_id,
        "State": state
    }
    return command


def confirm_anomaly(drone):
    """Issue command to drone to confirm the anomaly."""
    drone["State"]["Status"] = "Confirming"
    command = gen_Command(drone["State"])
    return command


def get_command_collection():
    """Get command collection from the central server."""
    try:
        get_command_collection_ = RES_CS.find_suitable_operation(
            None, None, CENTRAL_SERVER.CommandCollection)
        resp, body = get_command_collection_()
        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

        body = json.loads(body.decode('utf-8'))
        return body["members"]
    except Exception as e:
        print(e)
        return None


def create_command(command):
    """Add a command entity to the central server."""
    try:
        create_command_ = RES_CS.find_suitable_operation(
            SCHEMA.AddAction, CENTRAL_SERVER.Command)
        resp, body = create_command_(command)

        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
        new_command = Resource.from_iri(resp['location'])
        print("Command created successfully.")
        return new_command
    except Exception as e:
        print(e)
        return None


def issue_command(RES, Namespace_, command):
    """Issue Commands to Drones."""
    try:
        issue_command_ = RES.find_suitable_operation(
            SCHEMA.AddAction, Namespace_.Command)
        resp, body = issue_command_(command)

        assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
        new_command = Resource.from_iri(resp['location'])
        print("Command issued successfully.")
        return new_command
    except Exception as e:
        print(e)
        return None
