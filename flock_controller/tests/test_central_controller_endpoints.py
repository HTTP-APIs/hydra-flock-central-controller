""" Tests for checking if all the drone endpoints are working properly."""

import unittest
import requests
import json
import os
from flock_controller.mechanics.main import gen_State, ordered
from flock_controller.mechanics.location import gen_Location
from flock_controller.mechanics.commands import gen_Command

CS_URL = "http://localhost:8080/"


class TestCSRequests(unittest.TestCase):
    """Test Class for requests on Central Server."""

    def test_request_vocab(self):
        """Test the central server vocab."""
        request_get = requests.get(CS_URL + 'api/vocab')
        request_put = requests.put(
            CS_URL + 'api/vocab', data=json.dumps(dict(foo='bar')))
        request_post = requests.post(
            CS_URL + 'api/vocab', data=json.dumps(dict(foo='bar')))
        request_delete = requests.delete(CS_URL + 'api/vocab')
        assert request_get.status_code == 200
        assert request_put.status_code == 405
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_entrypoint(self):
        """Test the central server entrypoint."""
        request_get = requests.get(CS_URL + 'api/')
        request_put = requests.put(
            CS_URL + 'api/', data=json.dumps(dict(foo='bar')))
        request_post = requests.post(
            CS_URL + 'api/', data=json.dumps(dict(foo='bar')))
        request_delete = requests.delete(CS_URL + 'api/')
        assert request_get.status_code == 200
        assert request_put.status_code == 405
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_location(self):
        """Test the Area endpoint."""
        location = gen_Location("0,0")

        request_get = requests.get(CS_URL + 'api/Location')
        request_put = requests.put(
            CS_URL + 'api/Location', data=json.dumps(location))
        request_post = requests.post(
            CS_URL + 'api/Location', data=json.dumps(location))
        request_delete = requests.delete(CS_URL + 'api/Location')
        # 404 if area is not set use mechanics.update_area to set area.
        assert request_get.status_code in [200, 404]
        assert request_put.status_code == 201
        assert request_post.status_code in [200, 201]
        assert request_delete.status_code == 405

    def test_request_command_collection(self):
        """Test the CommandCollection endpoint."""
        state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
        command = gen_Command(-1000, state)

        request_get = requests.get(CS_URL + 'api/CommandCollection')
        request_put = requests.put(
            CS_URL + 'api/CommandCollection', data=json.dumps(command))
        request_post = requests.post(
            CS_URL + 'api/CommandCollection', data=json.dumps(command))
        request_delete = requests.delete(CS_URL + 'api/CommandCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_datastream_collection(self):
        """Test the DatastreamCollection endpoint."""
        request_get = requests.get(CS_URL + 'api/DatastreamCollection')
        request_put = requests.put(CS_URL + 'api/DatastreamCollection',
                                   data=json.dumps({"DroneID": "1", "@type": "Datastream"}))
        request_post = requests.post(CS_URL + 'api/DatastreamCollection',
                                     data=json.dumps({"DroneID": "1", "@type": "Datastream"}))
        request_delete = requests.delete(CS_URL + 'api/DatastreamCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_drone_collection(self):
        """Test the DroneCollection endpoint."""
        request_get = requests.get(CS_URL + 'api/DroneCollection')
        request_put = requests.put(CS_URL + 'api/DroneCollection',
                                   data=json.dumps({"name": "test_drone", "@type": "Drone"}))
        request_post = requests.post(
            CS_URL + 'api/DroneCollection', data=json.dumps({"name": "test_drone", "@type": "Drone"}))
        request_delete = requests.delete(CS_URL + 'api/DroneCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_controller_log_collection(self):
        """Test the LogEntryCollection endpoint."""
        request_get = requests.get(CS_URL + 'api/ControllerLogCollection')
        request_put = requests.put(CS_URL + 'api/ControllerLogCollection',
                                   data=json.dumps({"@type": "ControllerLog", "LogString": "Test Log"}))
        request_post = requests.post(CS_URL + 'api/ControllerLogCollection',
                                     data=json.dumps({"@type": "ControllerLog", "LogString": "Test Log"}))
        request_delete = requests.delete(
            CS_URL + 'api/ControllerLogCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_drone_log_collection(self):
        """Test the LogEntryCollection endpoint."""
        request_get = requests.get(CS_URL + 'api/DroneLogCollection')
        request_put = requests.put(CS_URL + 'api/DroneLogCollection',
                                   data=json.dumps({"@type": "DroneLog", "LogString": "Test Log"}))
        request_post = requests.post(CS_URL + 'api/DroneLogCollection',
                                     data=json.dumps({"@type": "DroneLog", "LogString": "Test Log"}))
        request_delete = requests.delete(CS_URL + 'api/DroneLogCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_http_api_log_collection(self):
        """Test the LogEntryCollection endpoint."""
        request_get = requests.get(CS_URL + 'api/HttpApiLogCollection')
        request_put = requests.put(CS_URL + 'api/HttpApiLogCollection',
                                   data=json.dumps({"@type": "HttpApiLog", "Subject": "Test Log"}))
        request_post = requests.post(CS_URL + 'api/HttpApiLogCollection',
                                     data=json.dumps({"@type": "HttpApiLog", "Subject": "Test Log"}))
        request_delete = requests.delete(CS_URL + 'api/HttpApiLogCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_message_collection(self):
        """Test the MessageCollection endpoint."""
        request_get = requests.get(CS_URL + 'api/MessageCollection')
        request_put = requests.put(CS_URL + 'api/MessageCollection',
                                   data=json.dumps({"@type": "Message", "MessageString": "Test message"}))
        request_post = requests.post(CS_URL + 'api/MessageCollection',
                                     data=json.dumps({"@type": "Message", "MessageString": "Test message"}))
        request_delete = requests.delete(CS_URL + 'api/MessageCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_command_collection_wrong_type_put(self):
        """Test the CommandCollection endpoint PUT with wrong type ."""
        state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
        command = gen_Command(-1000, state)
        command["@type"] = "Dummy"

        request_put = requests.put(
            CS_URL + 'api/CommandCollection', data=json.dumps(command))
        assert request_put.status_code == 400

    def test_request_datastream_collection_wrong_type_put(self):
        """Test the DatastreamCollection endpoint PUT with wrong object type."""
        request_put = requests.put(CS_URL + 'api/DatastreamCollection',
                                   data=json.dumps({"hello": "World", "@type": "Dummy"}))
        assert request_put.status_code == 400

    def test_request_drone_collection_wrong_type_put(self):
        """Test the DroneCollection endpoint PUT with wrong object type."""
        request_put = requests.put(CS_URL + 'api/DroneCollection',
                                   data=json.dumps({"name": "test_drone", "@type": "Dummy"}))
        assert request_put.status_code == 400

    def test_request_drone_log_collection_wrong_type_put(self):
        """Test the LogEntryCollection endpoint PUT with wrong object type."""
        request_put = requests.put(CS_URL + 'api/DroneLogCollection',
                                   data=json.dumps({"@type": "Dummy", "LogString": "Test Log"}))
        assert request_put.status_code == 400

    def test_request_drone_log_collection_wrong_property_put(self):
        """Test the LogEntryCollection endpoint PUT with wrong object type."""
        request_put = requests.put(CS_URL + 'api/DroneLogCollection',
                                   data=json.dumps({"@type": "DroneLog", "Log": "Test Log"}))
        assert request_put.status_code == 400

    def test_request_http_api_log_collection_wrong_type_put(self):
        """Test the LogEntryCollection endpoint PUT with wrong object type."""
        request_put = requests.put(CS_URL + 'api/HttpApiLogCollection',
                                   data=json.dumps({"@type": "Dummy", "Log": "Test Log"}))
        assert request_put.status_code == 400

    def test_request_http_api_log_collection_wrong_property_put(self):
        """Test the LogEntryCollection endpoint PUT with wrong object type."""
        request_put = requests.put(CS_URL + 'api/HttpApiLogCollection',
                                   data=json.dumps({"@type": "HttpApiLog", "Log": "Test Log"}))
        assert request_put.status_code == 400

    def test_request_controller_log_collection_wrong_type_put(self):
        """Test the LogEntryCollection endpoint PUT with wrong object type."""
        request_put = requests.put(CS_URL + 'api/ControllerLogCollection',
                                   data=json.dumps({"@type": "Dummy", "Log": "Test Log"}))
        assert request_put.status_code == 400

    def test_request_controller_log_collection_wrong_type_put(self):
        """Test the LogEntryCollection endpoint PUT with wrong object type."""
        request_put = requests.put(CS_URL + 'api/ControllerLogCollection',
                                   data=json.dumps({"@type": "ControllerLog", "Log": "Test Log"}))
        assert request_put.status_code == 400

    def test_request_message_collection_wrong_type_put(self):
        """Test the MessageCollection endpoint PUT with wrong object type."""
        request_put = requests.put(CS_URL + 'api/MessageCollection',
                                   data=json.dumps({"@type": "Dummy", "message": "Test message"}))
        assert request_put.status_code == 400

    def test_location_data(self):
        """Test if location submitted is same as location received back."""
        location = gen_Location("5,5")
        request_post = requests.post(
            CS_URL + 'api/Location', data=json.dumps(location))
        request_get = requests.get(CS_URL + 'api/Location')
        received_location = request_get.json()
        received_location.pop("@id", None)
        received_location.pop("@context", None)

        assert request_post.status_code in [201, 200]
        assert ordered(location) == ordered(received_location)


if __name__ == '__main__':
    message = """
    Running tests for the app. Checking if all responses are in proper order.
    NOTE: This doesn't ensure that data is entered or deleted in a proper manner.
    It only checks the format of the reponses.
    """
    print(message)
    unittest.main()
