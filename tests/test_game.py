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


def test_menu(client):  # for base.html or the menu template
    response = client.get('/')
    assert b'This is ww2mania text adventure game' in response.data
    assert b'Please choose a menu option and proceed' in response.data
    assert b'Start Game' in response.data
    assert b'How To Play' in response.data


def how_to_play_test(client):  # for the howtoplay template
    response = client.get('/game/howtoplay')
    assert b'Here is how to play ww2mania' in response.data
    assert b'Back to Menu' in response.data
    assert b'So the rules are simple.' in response.data


def test_game1(client):  # for the welcome template
    response = client.get('/game/welcome')
    assert b'Exit Game' in response.data
    assert b'Welcome' in response.data
    assert b'You are about to be deployed' in response.data
    assert b'Answer the question soldier!' in response.data


def test_game2(client):  # for the office template
    response = client.get('/game/office')
    assert b'Exit Game' in response.data
    assert b'Welcome to the sgts office' in response.data
    assert b'Answer the question soldier!' in response.data


def test_game3(client):  # for the jail template
    response = client.get('/game/jail')
    assert b'This is your life now boy, this is your home.' in response.data
    assert b'Jail dude' in response.data
    assert b'Answer the question soldier!' in response.data


def test_game4(client):
    response = client.get('/game/dead')
    assert b'You have died in battle' in response.data
    assert b'Exit Game' in response.data
    assert b'You are with your dead brothers' in response.data


def test_airforce_room(client):
    response = client.get('/game/airforce')
    assert b'Alright so you are flying with us' in response.data
    assert b'You will be starting trainging on piloting soon' in response.data
    assert b'Exit Game' in response.data
    assert b'Answer the question soldier!' in response.data


def test_army_room(client):
    response = client.get('game/army')
    assert b'Wooo aaaah, welcome to the army maggot.' in response.data
    assert b'Basic training will start soon but give me 50 push ups first'
    assert b'Exit Game' in response.data
    assert b'Answer the question soldier!' in response.data


def test_navy_room(client):
    response = client.get('game/navy')
    assert b'Howdy, how you doing?' in response.data
    assert b'So you picked the navy what a fine choice' in response.data
    assert b'So we dont really have time to train you here is you uniform see you at base' in response.data
    assert b'Exit Game' in response.data
    assert b'Answer the question soldier!' in response.data


def test_jail_room(client):
    response = client.get('game/jail')
    assert b'Jail dude' in response.data
    assert b'Exit Game' in response.data
    assert b'Answer the question soldier!' in response.data


def test_jail_read(client):
    response = client.get('game/jailRead')
    assert b'You read 10 pages of the Dictionary it was pleasent.' in response.data
    assert b'Only 824 days to go' in response.data
    assert b'Exit Game' in response.data
    assert b'Answer the question soldier!' in response.data


def test_jail_sleep(client):
    response = client.get('game/jailSleep')
    assert b'You only got 3 hours of sleep if only the guys would stop yelling' in response.data
    assert b'Only 824 days to go' in response.data
    assert b'Exit Game' in response.data
    assert b'Answer the question soldier!' in response.data


def test_jail_restroom(client):
    response = client.get('game/jailRestroom')
    assert b'Exit Game' in response.data
    assert b'You used the restroom it was not so nice. Your cell mate was watching.' in response.data
    assert b'Only 824 days to go' in response.data
    assert b'Answer the question soldier' in response.data
