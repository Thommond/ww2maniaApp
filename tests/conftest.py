import pytest
from ww2maniaApp import create_app


with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    app = create_app({

        'TESTING': True

    })
    # TODO: database setup

    yield app

    # TODO: database teardown


@pytest.fixture
def client(app):
    return app.test_client()
