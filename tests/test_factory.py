import pytest
from ww2maniaApp import create_app


def test_config():  # Testing if conftest.py is testing correctly
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_index(client):  # Testing if the demo still works
    response = client.get('/Demo')
    assert response.data == b'Flask Heroku Demo'
