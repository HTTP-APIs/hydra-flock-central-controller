"""
Generated API Documentation for Server API using server_doc_gen.py."""

doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "hydra:description",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "expectsHeader": "hydra:expectsHeader",
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "label": "rdfs:label",
        "manages": "hydra:manages",
        "method": "hydra:method",
        "possibleStatus": "hydra:possibleStatus",
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "readable": "hydra:readable",
        "required": "hydra:required",
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "returnsHeader": "hydra:returnsHeader",
        "statusCode": "hydra:statusCode",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "vocab": "http://localhost:8080/api/vocab#",
        "writeable": "hydra:writeable"
    },
    "@id": "http://localhost:8080/api/vocab",
    "@type": "ApiDocumentation",
    "description": "API Documentation for the server side system",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "vocab:Drone",
            "@type": "hydra:Class",
            "description": "Class for a drone",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Drone",
                    "expectsHeader": [
                        {
                            "description": "Drone updated",
                            "statusCode": 200
                        }
                    ],
                    "method": "POST",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "SubmitDrone"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Drone",
                    "expectsHeader": [
                        {
                            "description": "Drone updated",
                            "statusCode": 200
                        }
                    ],
                    "method": "PUT",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "UpdateDrone"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "Drone not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Drone Returned",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:Drone",
                    "returnsHeader": [],
                    "title": "GetDrone"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "Drone not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Drone successfully deleted.",
                            "statusCode": 200
                        }
                    ],
                    "method": "DELETE",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "DeleteDrone"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:State",
                    "readable": "false",
                    "required": "true",
                    "title": "State",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/name",
                    "readable": "false",
                    "required": "true",
                    "title": "name",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/model",
                    "readable": "false",
                    "required": "true",
                    "title": "model",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readable": "false",
                    "required": "true",
                    "title": "MaxSpeed",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/device",
                    "readable": "false",
                    "required": "true",
                    "title": "Sensor",
                    "writeable": "false"
                }
            ],
            "title": "Drone"
        },
        {
            "@id": "vocab:State",
            "@type": "hydra:Class",
            "description": "Class for drone state objects",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "State not found",
                            "statusCode": 404
                        },
                        {
                            "description": "State Returned",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:State",
                    "returnsHeader": [],
                    "title": "GetState"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readable": "false",
                    "required": "true",
                    "title": "Speed",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": "false",
                    "required": "true",
                    "title": "Position",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/Property",
                    "readable": "false",
                    "required": "true",
                    "title": "Direction",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/fuelCapacity",
                    "readable": "false",
                    "required": "true",
                    "title": "Battery",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/status",
                    "readable": "false",
                    "required": "true",
                    "title": "Status",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": "false",
                    "required": "true",
                    "title": "DroneID",
                    "writeable": "false"
                }
            ],
            "title": "State"
        },
        {
            "@id": "vocab:Datastream",
            "@type": "hydra:Class",
            "description": "Class for a datastream entry",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "Data not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Data returned",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:Datastream",
                    "returnsHeader": [],
                    "title": "ReadDatastream"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/QuantitativeValue",
                    "readable": "false",
                    "required": "true",
                    "title": "Temperature",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": "false",
                    "required": "true",
                    "title": "DroneID",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": "false",
                    "required": "true",
                    "title": "Position",
                    "writeable": "false"
                }
            ],
            "title": "Datastream"
        },
        {
            "@id": "vocab:DroneLog",
            "@type": "hydra:Class",
            "description": "Class for a drone log entry",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "DroneLog not found",
                            "statusCode": 404
                        },
                        {
                            "description": "DroneLog returned",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:DroneLog",
                    "returnsHeader": [],
                    "title": "ReadDroneLog"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": "false",
                    "required": "true",
                    "title": "DroneID",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/Text",
                    "readable": "false",
                    "required": "true",
                    "title": "LogString",
                    "writeable": "false"
                }
            ],
            "title": "DroneLog"
        },
        {
            "@id": "vocab:ControllerLog",
            "@type": "hydra:Class",
            "description": "Class for a controller log entry",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "ControllerLog not found",
                            "statusCode": 404
                        },
                        {
                            "description": "ControllerLog returned",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:ControllerLog",
                    "returnsHeader": [],
                    "title": "ReadControllerLog"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/Text",
                    "readable": "false",
                    "required": "true",
                    "title": "LogString",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": "false",
                    "required": "true",
                    "title": "DroneID",
                    "writeable": "false"
                }
            ],
            "title": "ControllerLog"
        },
        {
            "@id": "vocab:HttpApiLog",
            "@type": "hydra:Class",
            "description": "Class for a http api log entry",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "HttpApiLog not found",
                            "statusCode": 404
                        },
                        {
                            "description": "HttpApiLog returned",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:HttpApiLog",
                    "returnsHeader": [],
                    "title": "ReadHttpApiLog"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": "false",
                    "required": "true",
                    "title": "Subject",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/Action",
                    "readable": "false",
                    "required": "true",
                    "title": "Predicate",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": "false",
                    "required": "true",
                    "title": "Object",
                    "writeable": "false"
                }
            ],
            "title": "HttpApiLog"
        },
        {
            "@id": "vocab:Location",
            "@type": "hydra:Class",
            "description": "Class for location of the central controller.",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Location",
                    "expectsHeader": [
                        {
                            "description": "Controller location updated successfully.",
                            "statusCode": 200
                        }
                    ],
                    "method": "POST",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "UpdateLocation"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Location",
                    "expectsHeader": [
                        {
                            "description": "Controller location added successfully.",
                            "statusCode": 200
                        }
                    ],
                    "method": "PUT",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "AddLocation"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "Location of Controller not found.",
                            "statusCode": 404
                        },
                        {
                            "description": "Location of controller returned.",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:Location",
                    "returnsHeader": [],
                    "title": "GetLocation"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readable": "false",
                    "required": "true",
                    "title": "Location",
                    "writeable": "false"
                }
            ],
            "title": "Location"
        },
        {
            "@id": "vocab:Command",
            "@type": "hydra:Class",
            "description": "Class for drone commands",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "Command not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Command Returned",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:Command",
                    "returnsHeader": [],
                    "title": "GetCommand"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Command",
                    "expectsHeader": [
                        {
                            "description": "Command added",
                            "statusCode": 201
                        }
                    ],
                    "method": "PUT",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "AddCommand"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": "false",
                    "required": "true",
                    "title": "DroneID",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:State",
                    "readable": "false",
                    "required": "true",
                    "title": "State",
                    "writeable": "false"
                }
            ],
            "title": "Command"
        },
        {
            "@id": "vocab:Message",
            "@type": "hydra:Class",
            "description": "Class for messages received by the GUI interface",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "Message not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Message returned",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:Message",
                    "returnsHeader": [],
                    "title": "GetMessage"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "Message not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Message successfully deleted.",
                            "statusCode": 200
                        }
                    ],
                    "method": "DELETE",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "DeleteMessage"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/Text",
                    "readable": "false",
                    "required": "true",
                    "title": "MessageString",
                    "writeable": "false"
                }
            ],
            "title": "Message"
        },
        {
            "@id": "vocab:Anomaly",
            "@type": "hydra:Class",
            "description": "Class for Temperature anomalies that need to be confirmed",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "Anomaly not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Anomaly returned",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:Anomaly",
                    "returnsHeader": [],
                    "title": "GetAnomaly"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Anomaly",
                    "expectsHeader": [
                        {
                            "description": "Anomaly added successfully.",
                            "statusCode": 200
                        }
                    ],
                    "method": "PUT",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "AddAnomaly"
                },
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Anomaly",
                    "expectsHeader": [
                        {
                            "description": "Anomaly updated successfully.",
                            "statusCode": 201
                        }
                    ],
                    "method": "POST",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "UpdateAnomaly"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": "null",
                    "expectsHeader": [
                        {
                            "description": "Anomaly not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Anomaly successfully deleted.",
                            "statusCode": 200
                        }
                    ],
                    "method": "DELETE",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "DeleteAnomaly"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Location",
                    "readable": "false",
                    "required": "true",
                    "title": "Location",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": "false",
                    "required": "true",
                    "title": "DroneID",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/eventStatus",
                    "readable": "false",
                    "required": "true",
                    "title": "Status",
                    "writeable": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readable": "false",
                    "required": "true",
                    "title": "AnomalyID",
                    "writeable": "false"
                }
            ],
            "title": "Anomaly"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "Resource"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "null",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "Collection"
        },
        {
            "@id": "vocab:DroneCollection",
            "@type": "hydra:Class",
            "description": "A collection of drone",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:drone_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Drone entities",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:DroneCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:drone_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Drone entity",
                    "expects": "vocab:Drone",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the Drone entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:Drone",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The drone",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "DroneCollection"
        },
        {
            "@id": "vocab:StateCollection",
            "@type": "hydra:Class",
            "description": "A collection of state",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:state_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all State entities",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:StateCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:state_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new State entity",
                    "expects": "vocab:State",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the State entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:State",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The state",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "StateCollection"
        },
        {
            "@id": "vocab:DatastreamCollection",
            "@type": "hydra:Class",
            "description": "A collection of datastream",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:datastream_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Datastream entities",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:DatastreamCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:datastream_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Datastream entity",
                    "expects": "vocab:Datastream",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the Datastream entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:Datastream",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The datastream",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "DatastreamCollection"
        },
        {
            "@id": "vocab:DroneLogCollection",
            "@type": "hydra:Class",
            "description": "A collection of dronelog",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:dronelog_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all DroneLog entities",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:DroneLogCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:dronelog_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new DroneLog entity",
                    "expects": "vocab:DroneLog",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the DroneLog entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:DroneLog",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The dronelog",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "DroneLogCollection"
        },
        {
            "@id": "vocab:ControllerLogCollection",
            "@type": "hydra:Class",
            "description": "A collection of controllerlog",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:controllerlog_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all ControllerLog entities",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:ControllerLogCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:controllerlog_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new ControllerLog entity",
                    "expects": "vocab:ControllerLog",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the ControllerLog entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:ControllerLog",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The controllerlog",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "ControllerLogCollection"
        },
        {
            "@id": "vocab:HttpApiLogCollection",
            "@type": "hydra:Class",
            "description": "A collection of httpapilog",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:httpapilog_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all HttpApiLog entities",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:HttpApiLogCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:httpapilog_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new HttpApiLog entity",
                    "expects": "vocab:HttpApiLog",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the HttpApiLog entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:HttpApiLog",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The httpapilog",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "HttpApiLogCollection"
        },
        {
            "@id": "vocab:CommandCollection",
            "@type": "hydra:Class",
            "description": "A collection of command",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:command_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Command entities",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:CommandCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:command_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Command entity",
                    "expects": "vocab:Command",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the Command entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:Command",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The command",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "CommandCollection"
        },
        {
            "@id": "vocab:MessageCollection",
            "@type": "hydra:Class",
            "description": "A collection of message",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:message_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Message entities",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:MessageCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:message_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Message entity",
                    "expects": "vocab:Message",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the Message entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:Message",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The message",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "MessageCollection"
        },
        {
            "@id": "vocab:AnomalyCollection",
            "@type": "hydra:Class",
            "description": "A collection of anomaly",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:anomaly_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Anomaly entities",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:AnomalyCollection",
                    "returnsHeader": []
                },
                {
                    "@id": "_:anomaly_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Anomaly entity",
                    "expects": "vocab:Anomaly",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the Anomaly entity was createdsuccessfully.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "vocab:Anomaly",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The anomaly",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "AnomalyCollection"
        },
        {
            "@id": "vocab:EntryPoint",
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "supportedOperation": [
                {
                    "@id": "_:entry_point",
                    "@type": "vocab:EntryPoint",
                    "description": "The APIs main entry point.",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The Location Class",
                    "hydra:title": "location",
                    "property": {
                        "@id": "vocab:EntryPoint/Location",
                        "@type": "hydra:Link",
                        "description": "Class for location of the central controller.",
                        "domain": "vocab:EntryPoint",
                        "label": "Location",
                        "range": "vocab:Location",
                        "supportedOperation": [
                            {
                                "@id": "updatelocation",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "null",
                                "expects": "vocab:Location",
                                "expectsHeader": [
                                    {
                                        "description": "Controller location updated successfully.",
                                        "statusCode": 200
                                    }
                                ],
                                "label": "UpdateLocation",
                                "method": "POST",
                                "possibleStatus": [],
                                "returns": "null",
                                "returnsHeader": []
                            },
                            {
                                "@id": "addlocation",
                                "@type": "http://schema.org/AddAction",
                                "description": "null",
                                "expects": "vocab:Location",
                                "expectsHeader": [
                                    {
                                        "description": "Controller location added successfully.",
                                        "statusCode": 200
                                    }
                                ],
                                "label": "AddLocation",
                                "method": "PUT",
                                "possibleStatus": [],
                                "returns": "null",
                                "returnsHeader": []
                            },
                            {
                                "@id": "getlocation",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "null",
                                "expectsHeader": [
                                    {
                                        "description": "Location of Controller not found.",
                                        "statusCode": 404
                                    },
                                    {
                                        "description": "Location of controller returned.",
                                        "statusCode": 200
                                    }
                                ],
                                "label": "GetLocation",
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:Location",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The DroneCollection collection",
                    "hydra:title": "dronecollection",
                    "property": {
                        "@id": "vocab:EntryPoint/DroneCollection",
                        "@type": "hydra:Link",
                        "description": "The DroneCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "DroneCollection",
                        "range": "vocab:DroneCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:drone_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Drone entities",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:DroneCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:drone_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Drone entity",
                                "expects": "vocab:Drone",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the Drone entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:Drone",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The StateCollection collection",
                    "hydra:title": "statecollection",
                    "property": {
                        "@id": "vocab:EntryPoint/StateCollection",
                        "@type": "hydra:Link",
                        "description": "The StateCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "StateCollection",
                        "range": "vocab:StateCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:state_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all State entities",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:StateCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:state_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new State entity",
                                "expects": "vocab:State",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the State entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:State",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The DatastreamCollection collection",
                    "hydra:title": "datastreamcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/DatastreamCollection",
                        "@type": "hydra:Link",
                        "description": "The DatastreamCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "DatastreamCollection",
                        "range": "vocab:DatastreamCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:datastream_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Datastream entities",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:DatastreamCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:datastream_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Datastream entity",
                                "expects": "vocab:Datastream",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the Datastream entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:Datastream",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The DroneLogCollection collection",
                    "hydra:title": "dronelogcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/DroneLogCollection",
                        "@type": "hydra:Link",
                        "description": "The DroneLogCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "DroneLogCollection",
                        "range": "vocab:DroneLogCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:dronelog_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all DroneLog entities",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:DroneLogCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:dronelog_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new DroneLog entity",
                                "expects": "vocab:DroneLog",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the DroneLog entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:DroneLog",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The ControllerLogCollection collection",
                    "hydra:title": "controllerlogcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/ControllerLogCollection",
                        "@type": "hydra:Link",
                        "description": "The ControllerLogCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "ControllerLogCollection",
                        "range": "vocab:ControllerLogCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:controllerlog_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all ControllerLog entities",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:ControllerLogCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:controllerlog_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new ControllerLog entity",
                                "expects": "vocab:ControllerLog",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the ControllerLog entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:ControllerLog",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The HttpApiLogCollection collection",
                    "hydra:title": "httpapilogcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/HttpApiLogCollection",
                        "@type": "hydra:Link",
                        "description": "The HttpApiLogCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "HttpApiLogCollection",
                        "range": "vocab:HttpApiLogCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:httpapilog_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all HttpApiLog entities",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:HttpApiLogCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:httpapilog_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new HttpApiLog entity",
                                "expects": "vocab:HttpApiLog",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the HttpApiLog entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:HttpApiLog",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The CommandCollection collection",
                    "hydra:title": "commandcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/CommandCollection",
                        "@type": "hydra:Link",
                        "description": "The CommandCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "CommandCollection",
                        "range": "vocab:CommandCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:command_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Command entities",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:CommandCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:command_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Command entity",
                                "expects": "vocab:Command",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the Command entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:Command",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The MessageCollection collection",
                    "hydra:title": "messagecollection",
                    "property": {
                        "@id": "vocab:EntryPoint/MessageCollection",
                        "@type": "hydra:Link",
                        "description": "The MessageCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "MessageCollection",
                        "range": "vocab:MessageCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:message_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Message entities",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:MessageCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:message_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Message entity",
                                "expects": "vocab:Message",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the Message entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:Message",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The AnomalyCollection collection",
                    "hydra:title": "anomalycollection",
                    "property": {
                        "@id": "vocab:EntryPoint/AnomalyCollection",
                        "@type": "hydra:Link",
                        "description": "The AnomalyCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "AnomalyCollection",
                        "range": "vocab:AnomalyCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:anomaly_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Anomaly entities",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:AnomalyCollection",
                                "returnsHeader": []
                            },
                            {
                                "@id": "_:anomaly_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Anomaly entity",
                                "expects": "vocab:Anomaly",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the Anomaly entity was createdsuccessfully.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "vocab:Anomaly",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                }
            ],
            "title": "EntryPoint"
        }
    ],
    "title": "API Doc for the server side API"
}
