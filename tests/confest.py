import pytest
from ww2mania import create_app


@pytest.fixture
def app():
    app = create_app({'TESTING': True})

    # TODO: database setup

    yield app

    # TODO: database teardown


@pytest.fixture
def client(app):
    return app.test_client()
