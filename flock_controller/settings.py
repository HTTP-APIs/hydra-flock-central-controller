import os

# Using sqlite as database
global DB_URL
db_path = os.path.join(os.path.dirname(__file__), 'database.db')
DB_URL = 'sqlite:///{}'.format(db_path)


global HYDRUS_SERVER_URL, PORT, API_NAME
HYDRUS_SERVER_URL = "http://localhost:8080/"
PORT = 8080
API_NAME = "api"

# Drone configuration
global CENTRAL_SERVER_NAMESPACE, DRONE1_NAMESPACE, DRONE2_NAMESPACE, DRONE3_NAMESPACE, DRONE4_NAMESPACE
CENTRAL_SERVER_NAMESPACE = "http://localhost:8080/api/vocab#"
DRONE1_NAMESPACE = "http://localhost:8081/api/vocab#"
DRONE2_NAMESPACE = "http://localhost:8082/api/vocab#"
DRONE3_NAMESPACE = "http://localhost:8083/api/vocab#"
DRONE4_NAMESPACE = "http://localhost:8084/api/vocab#"

global DRONE1_URL, DRONE2_URL, DRONE3_URL, DRONE4_URL, CENTRAL_SERVER_URL
DRONE1_URL = "http://localhost:8081"
DRONE2_URL = "http://localhost:8082"
DRONE3_URL = "http://localhost:8083"
DRONE4_URL = "http://localhost:8084"
CENTRAL_SERVER_URL = "http://localhost:8080"

global IRI_CS, IRI_DRONE1, IRI_DRONE2, IRI_DRONE3, IRI_DRONE4
IRI_CS = "http://localhost:8080/api"
IRI_DRONE1 = "http://localhost:8081/api"
IRI_DRONE2 = "http://localhost:8082/api"
IRI_DRONE3 = "http://localhost:8083/api"
IRI_DRONE4 = "http://localhost:8084/api"
