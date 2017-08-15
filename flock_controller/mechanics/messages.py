"""Operations for managing messages."""
from hydra import Resource, SCHEMA
from flock_controller.mechanics.main import CENTRAL_SERVER, RES_CS, IRI_CS
import json


def gen_Message(message):
    """Create a new Message."""
    message = {
        "@type": "Message",
        "MessageString": message,
    }
    return message


def get_message_collection():
    """Get order collection from the central server."""
    get_message_collection_ = RES_CS.find_suitable_operation(None, None, CENTRAL_SERVER.MessageCollection)
    resp, body = get_message_collection_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    body = json.loads(body.decode('utf-8'))
    return body["members"]


def create_message(message):
    """Add a message object entity to the central server."""
    create_message_ = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.Message)
    resp, body = create_message_(message)

    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    new_message = Resource.from_iri(resp['location'])
    print("Message created successfully.")
    return new_message


def get_message(id_):
    """Get the message details from the central controller given the drone ID."""
    IRI = IRI_CS + "/MessageCollection/" + str(id_)
    RES = Resource.from_iri(IRI)
    get_message_ = RES.find_suitable_operation(output_type=CENTRAL_SERVER.Message)
    resp, body = get_message_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    body = json.loads(body.decode('utf-8'))

    body.pop("@context")
    body.pop("@type")
    return body


def delete_message(id_):
    """Delete a message from the message collection at central controller given the message id."""
    try:
        i = Resource.from_iri(IRI_CS + "/MessageCollection/" + str(id_))
        resp, _ = i.find_suitable_operation(SCHEMA.DeleteAction)()
        print("RESP, RESP")
        if resp.status // 100 != 2:
            return "error deleting <%s>" % i.identifier
        else:
            return "deleted <%s>" % i.identifier
    except Exception as e:
        print(e)
        return {404: "Resource with Id %s not found!" % (id_,)}




if __name__ == "__main__":
    print(get_message_collection())
    message = gen_Message("Hello world")
    print(create_message(message))
    print(get_message(1))
