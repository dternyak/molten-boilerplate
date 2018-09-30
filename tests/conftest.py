import pytest
import toml
from molten import testing

from index import create_app

with open("settings.toml") as conffile:
    toml_data = toml.loads(conffile.read())


# requires function scope so that database is removed on every tests
# TODO - find a less hacky way to clear database after each test
@pytest.fixture(scope="function")
def app():
    app = create_app()
    yield app
    import os
    os.remove(toml_data["test"]["database_engine_dsn"].split('///')[1])


@pytest.fixture(scope="function")
def client(app):
    return testing.TestClient(app)


@pytest.fixture(scope="session")
def auth():
    def auth(request):
        request.headers["authorization"] = "Bearer secret"
        return request

    return auth
