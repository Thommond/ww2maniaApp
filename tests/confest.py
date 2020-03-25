import pytest
import os
import tempfile
import postgres
from ww2maniaApp import create_app
from ww2maniaApp.db import get_db, init_db


with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    dp_fd, db_path = tempfile.mkstemp()
    app = create_app({

        'TESTING': True,
        'DATABASE': db_path

    })
    # TODO: database setup

    yield app

    # TODO: database teardown
