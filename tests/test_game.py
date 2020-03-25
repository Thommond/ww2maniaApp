import pytest


def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'test\nbody'not in response.data
    assert b'Welcome soldier what is your name?' in response.data


def test_menu(client, game):
    response = client.get('/game/menu')
    assert b'This is ww2mania text adventure game' in response.data
    assert b'Please choose a menu option and proceed'
    assert b'Start game'
    assert b'How to play'


def test_game1(client, game):
    response = client.get('/game/room1')
    assert b'Exit Game'
    assert b'Welcome soldier'
    assert b'Please enter your answer in the form below'


def test_game2(client, game):
    response = client.get('/game/room2')
    assert b'Exit game'
    assert b'Strength'
    assert b'Swiftness'
    assert b'Luck'
    assert b'Intelligence'
    assert b'Charisma'
    assert b'Please enter your anser in the form below'
