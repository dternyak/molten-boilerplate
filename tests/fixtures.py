import pytest
from molten import testing

from index import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    yield app
    # TODO - find a less hacky way to clear database after each test
    import os
    test_db = "test.db.sqlite3"
    os.path.isfile(test_db)
    os.remove(test_db)


@pytest.fixture(scope="session")
def client(app):
    return testing.TestClient(app)


@pytest.fixture(scope="session")
def auth():
    def auth(request):
        request.headers["authorization"] = "Bearer secret"
        return request

    return auth
