"""Script for setting up Hydrus with flock_drone API Doc."""
from hydrus.app_factory import app_factory
from hydrus.utils import set_session, set_doc, set_hydrus_server_url
from hydrus.utils import set_authentication, set_token
# from hydrus.app import set_session, set_doc, set_hydrus_server_url
from hydrus.data import doc_parse
from hydra_python_core import doc_maker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hydrus.data.db_models import Base
from flock_controller.settings import DB_URL, PORT, HYDRUS_SERVER_URL, API_NAME
from gevent.pywsgi import WSGIServer


import os
from flock_controller.api_docs.doc import doc


if __name__ == "__main__":
    engine = create_engine(DB_URL)

    print("Droping database if exist")

    Base.metadata.drop_all(engine)

    print("Creating models....")
    Base.metadata.create_all(engine)
    print("Done")

    apidoc = doc_maker.create_doc(doc, HYDRUS_SERVER_URL, API_NAME)

    session = sessionmaker(bind=engine)()

    classes = doc_parse.get_classes(apidoc.generate())

    properties = doc_parse.get_all_properties(classes)

    doc_parse.insert_classes(classes, session)
    doc_parse.insert_properties(properties, session)

    app = app_factory(API_NAME)

    with set_doc(app, apidoc):
        with set_authentication(app, False):
            with set_token(app, True):
                with set_hydrus_server_url(app, HYDRUS_SERVER_URL):
                    with set_session(app, session):
                        http_server = WSGIServer(('', PORT), app)
                        http_server.serve_forever()
