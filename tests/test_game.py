import pytest

def test_menu(client):
    response = client.get('/game/')
    # Getting text data from menu page
    assert b'<h1>Ww2 Mania App</h1>' in response.data
    assert b'<p>Please choose a menu option and proceed</p>' in response.data
    assert b'Start Game' in response.data
    assert b'How To Play' in response.data



def how_to_play_test(client):
    assert client.get('/game/howtoplay').status_code == 200
    response = client.get('/game/howtoplay')
    # Getting text data from howtoplay page
    assert b'<h2>Here is how to play ww2mania</h2>' in response.data
    assert b'Back to Menu' in response.data
    assert b'So the rules are simple.' in response.data


def test_welcome(client):
    # Checking if user can get page
    assert client.get('/game/welcome').status_code == 200
    response = client.get('/game/welcome')
    #Testing if text renders on page
    assert b'Welcome' in response.data
    assert b'You are about to be deployed' in response.data
    # making post request
    response = client.post('/game/welcome', data={'answer': 'A'}, follow_redirects=True)
    # checking text data on new redirected page
    assert b'<h1>Sgts office</h1>' in response.data

    response = client.post('/game/welcome', data={'answer': 'B'}, follow_redirects=True)
    assert b'<h1>Jail dude</h1>' in response.data

    response = client.post('/game/welcome', data={'answer': 'fdslfjsd'}, follow_redirects=True)
    assert b'Welcome' in response.data


def test_office(client):
    # Testing to see if user can get page
    assert client.get('/game/office').status_code == 200
    response = client.get('/game/office')
    # See if text is on page
    assert b'<h1>Sgts office</h1>' in response.data
    assert b'Welcome to the sgts office' in response.data


#Checking some user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Army Recruitment</h1>'),
('B', b'<h1>Navy Recruitment</h1>'),
('C', b'<h1>Airforce Recruitment</h1>'),
('nonsense', b'<h1>Sgts office</h1>')
))

def test_office_posts(client, text, answer):
    # post request with data and see results on page
    response = client.post('/game/office', data={'answer': answer}, follow_redirects=True)
    assert text in response.data

def test_jail_room(client):  # for the jail template
    response = client.get('/game/jail')
    assert b'This is your life now boy, this is your home.' in response.data

# Checking some user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Jail Sleep</h1>'),
('B', b'<h1>Jail Reading</h1>'),
('C', b'<h1>Jail Rest Room</h1>'),
('this is a form', b'<h1>Jail dude</h1>')
))

def test_jail_room_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/jail', data={'answer': answer}, follow_redirects=True)
    assert text in response.data

def test_dead_room(client):
    assert client.get('/game/dead').status_code == 200
    response = client.get('/game/dead')
    assert b'You have died in battle' in response.data


def test_airforce_room(client):
    response = client.get('/game/airforce')
    assert b'Alright so you are flying with us' in response.data
    assert b'You will be starting trainging on piloting soon' in response.data

# Checking some user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Airforce Base</h1>'),
('B', b"<h1>Sgts office</h1>"),
('what is this', b'<h1>Airforce Recruitment</h1>')
))

def test_airforce_room_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/airforce', data={'answer': answer}, follow_redirects=True)
    assert text in response.data



def test_army_room(client):
    response = client.get('game/army')
    assert b'Wooo aaaah, welcome to the army maggot.' in response.data

# Checking some user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Push Ups</h1>'),
('B', b"<h1>Army Training</h1>"),
('C', b'<h1>Sgts office</h1>'),
('thifsdkfj', b'<h1>Army Recruitment</h1>')
))

def test_armyroom_room_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/army', data={'answer': answer}, follow_redirects=True)
    assert text in response.data


def test_navy_room(client):
    response = client.get('game/navy')
    assert b'Howdy, how you doing?' in response.data
    assert b'So you picked the navy what a fine choice' in response.data

# Checking user data
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Navy Deploy</h1>'),
('B', b'<h1>Sgts office</h1>'),
('thifsdkfj', b'<h1>Navy Recruitment</h1>')
))

def test_navy_room_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/navy', data={'answer': answer}, follow_redirects=True)
    assert text in response.data


def test_jail_read(client):
    response = client.get('game/jailRead')
    assert b'You read 10 pages of the Dictionary it was pleasent.' in response.data

# Checking user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Jail Sleep</h1>'),
('B', b'<h1>Jail Rest Room</h1>'),
('C', b'<h1>Sgts office</h1>'),
('D', b'<h1>You have died in battle</h1>'),
('thifsdkfj', b'<h1>Jail Reading</h1>')
))

def test_jail_read_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/jailRead', data={'answer': answer}, follow_redirects=True)
    assert text in response.data


def test_jail_sleep(client):
    response = client.get('game/jailSleep')
    assert b'You only got 3 hours of sleep if only the guys would stop yelling' in response.data

# Checking user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Jail Reading</h1>'),
('B', b'<h1>Jail Rest Room</h1>'),
('C', b'<h1>Sgts office</h1>'),
('D', b'<h1>You have died in battle</h1>'),
('thifsdkfj', b'<h1>Jail Sleep</h1>')
))

def test_jail_sleep_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/jailSleep', data={'answer': answer}, follow_redirects=True)
    assert text in response.data

def test_jail_restroom(client):
    response = client.get('game/jailRestroom')
    assert b'You used the restroom it was not so nice. Your cell mate was watching.' in response.data

# Checking user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Jail Sleep</h1>'),
('B', b'<h1>Jail Reading</h1>'),
('C', b'<h1>Sgts office</h1>'),
('D', b'<h1>You have died in battle</h1>'),
('thifsdkfj', b'<h1>Jail Rest Room</h1>')
))

def test_jail_restroom_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/jailRestroom', data={'answer': answer}, follow_redirects=True)
    assert text in response.data

def test_push_up(client):
    response = client.get('/game/pushUps')
    assert b'Push ups are' in response.data

# Checking user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Congrats!</h1>'),
('thifsdkfj', b'<h1>Push Ups</h1>')
))

def test_push_ups_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/pushUps', data={'answer': answer}, follow_redirects=True)
    assert text in response.data

def test_navy_deploy(client):
    response = client.get('/game/navyDeploy')
    assert b'Well It is time' in response.data

# Checking user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Congrats!</h1>'),
('B', b'<h1>Jail dude</h1>'),
('thifsdkfj', b'<h1>Navy Deploy</h1>')
))

def test_navy_deploy_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/navyDeploy', data={'answer': answer}, follow_redirects=True)
    assert text in response.data

def test_army_train(client):
    response = client.get('/game/armyTrain')
    assert b'We are on our' in response.data

# Checking user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Congrats!</h1>'),
('B', b'<h1>Jail dude</h1>'),
('thifsdkfj', b'<h1>Army Training</h1>')
))

def test_army_train_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/armyTrain', data={'answer': answer}, follow_redirects=True)
    assert text in response.data

def test_airforce_base(client):
    response = client.get('/game/airforceBase')
    assert b'Airforce is happy' in response.data


# Checking user input
@pytest.mark.parametrize(('answer', 'text'),(
('A', b'<h1>Congrats!</h1>'),
('thifsdkfj', b'<h1>Airforce Base</h1>')
))

def test_airforce_base_posts(client, text, answer):
    #post request with data and see results on page
    response = client.post('/game/airforceBase', data={'answer': answer}, follow_redirects=True)
    assert text in response.data
