import pytest
from molten import testing
from molten.contrib.sqlalchemy import (
    EngineData)

from db import Base
from index import create_app


def init_db(engine_data: EngineData):
    Base.metadata.create_all(engine_data.engine)


def setup_db(app):
    # Initialize the DB by injecting EngineData into init_db and calling it.
    resolver = app.injector.get_resolver()
    resolver.resolve(init_db)()


# requires function scope so that database is removed on every tests
# TODO - find a less hacky way to clear database after each test
@pytest.fixture(scope="function")
def app():
    app = create_app()
    setup_db(app)
    yield app
    import os
    test_db = "test.db.sqlite3"
    os.path.isfile(test_db)
    os.remove(test_db)


@pytest.fixture(scope="function")
def client(app):
    return testing.TestClient(app)


@pytest.fixture(scope="session")
def auth():
    def auth(request):
        request.headers["authorization"] = "Bearer secret"
        return request

    return auth
