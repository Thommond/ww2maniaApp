from ww2maniaApp import create_app
import pytest


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_index(client):
    response = client.get('/Demo')
    assert response.data == b'Flask Heroku Demo'
