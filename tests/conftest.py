import pytest
from molten import testing

from index import create_app


# requires function scope so that database is removed on every tests
# TODO - find a less hacky way to clear database after each test
@pytest.fixture(scope="function")
def app():
    app = create_app(_setup_db=True)
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
