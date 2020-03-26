

def log_check():
    assert b'Log in' in response.data
    assert b'register' in response.data
    assert b'ww2mania' in response.data


def register_check():
    assert b'register' in response.data
    assert b'ww2mania' in response.data
    assert b'already a user log in' in reponse.data
