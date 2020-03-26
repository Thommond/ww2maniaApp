import pytest


# def test_index(client):
#     response = client.get('/')
#     assert b"Log In" in response.data
#     assert b"Register" in response.data
#
#     auth.login()
#     response = client.get('/')
#     assert b'Log Out' in response.data
#     assert b'test title' in response.data
#     assert b'test\nbody'not in response.data
#     assert b'Welcome soldier what is your name?' in response.data


def test_menu(client, game):
    response = client.get('/game/menu')
    assert b'This is ww2mania text adventure game' in response.data
    assert b'Please choose a menu option and proceed'
    assert b'Start game'
    assert b'How to play'


def test_game1(client, game):
    response = client.get('/game/welcome')
    assert b'Exit Game'
    assert b'Welcome soldier'
    assert b'Please enter your answer in the form below'


def test_game2(client, game):
    response = client.get('/game/stats')
    assert b'Exit Game'
    assert b'Time to choose your stats'
    assert 'Please enter your answer in the form below'
