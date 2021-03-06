import functools
from flask import (
    Blueprint, Flask, redirect, request, render_template, url_for
)
import ww2maniaApp.items

import ww2maniaApp.char

import ww2maniaApp.room


bp = Blueprint('game', __name__, url_prefix='/game')


@bp.route('/')
def menu():
    # Choose info about game or to play game
    return render_template('base.html')


@bp.route('/howtoplay', methods=('GET', 'POST'))
def howtoplay():
    # Learns to play game and goes back to menu
    return render_template('game/howToPlay.html')

# The first room in the game
@bp.route('/welcome', methods=('GET', 'POST'))
def welcome():

    if request.method == 'POST':
        answer = request.form['answer']

        if answer == "A":
            return redirect(url_for('game.office_room'))
        elif answer == "B":
            return redirect(url_for('game.jail_room'))
        else:
            return redirect(url_for('game.welcome'))  # if they do not supply

    return render_template('game/room.html', title=ww2maniaApp.room.welcome.name, message=ww2maniaApp.room.welcome.message)

# This is where players are routed if they died in the game.
# To restart they can press the exit game button on the top right of each template
@bp.route('/dead', methods=('GET', 'POST'))
def dead_room():
    # Your dead nothing happens
    return render_template('game/room.html', title=ww2maniaApp.room.dead.name, message=ww2maniaApp.room.dead.message)

# The office is where the players choose their stats
@bp.route('/office', methods=('GET', 'POST'))
def office_room():
    if request.method == 'POST':
        answer = request.form['answer']

        if answer == "A":
            return redirect(url_for('game.army_room'))
        elif answer == "B":
            return redirect(url_for('game.navy_room'))
        elif answer == "C":
            return redirect(url_for('game.airforce_room'))
        else:
            return redirect(url_for('game.office_room'))

    return render_template('game/room.html', title=ww2maniaApp.room.office.name, message=ww2maniaApp.room.office.message)

# Jail is a game if you choose to go to jail in the first answer you make
@bp.route('/jail', methods=('GET', 'POST'))
def jail_room():

    if request.method == 'POST':
        answer = request.form['answer']

        if answer == "A":
            return redirect(url_for('game.jail_sleep'))
        elif answer == "B":
            return redirect(url_for('game.jail_read'))

        elif answer == "C":
            return redirect(url_for('game.jail_restroom'))
        else:
            return redirect(url_for('game.jail_room'))  # if they do not supply

    return render_template('game/room.html', title=ww2maniaApp.room.jail.name, message=ww2maniaApp.room.jail.message)


@bp.route('/jailRead', methods=('GET', 'POST'))
def jail_read():

    if request.method == 'POST':
        answer = request.form['answer']

        if answer == "A":
            return redirect(url_for('game.jail_sleep'))
        elif answer == "B":
            return redirect(url_for('game.jail_restroom'))
        elif answer == "C":
            return redirect(url_for('game.office_room'))
        elif answer == "D":
            return redirect(url_for('game.dead_room'))
        else:
            return redirect(url_for('game.jail_read'))

    return render_template('game/room.html', title=ww2maniaApp.room.jail_read.name, message=ww2maniaApp.room.jail_read.message)


@bp.route('/jailSleep', methods=('GET', 'POST'))
def jail_sleep():

    if request.method == 'POST':
        answer = request.form['answer']

        if answer == "A":
            return redirect(url_for('game.jail_read'))
        elif answer == "B":
            return redirect(url_for('game.jail_restroom'))
        elif answer == "C":
            return redirect(url_for('game.office_room'))
        elif answer == "D":
            return redirect(url_for('game.dead_room'))
        else:
            return redirect(url_for('game.jail_sleep'))

    return render_template('game/room.html', title=ww2maniaApp.room.jail_sleep.name, message=ww2maniaApp.room.jail_sleep.message)


@bp.route('/jailRestroom', methods=('GET', 'POST'))
def jail_restroom():

    if request.method == 'POST':
        answer = request.form['answer']

        if answer == "A":
            return redirect(url_for('game.jail_sleep'))
        elif answer == "B":
            return redirect(url_for('game.jail_read'))
        elif answer == "C":
            return redirect(url_for('game.office_room'))
        elif answer == "D":
            return redirect(url_for('game.dead_room'))
        else:
            return redirect(url_for('game.jail_restroom'))

    return render_template('game/room.html', title=ww2maniaApp.room.jail_restroom.name, message=ww2maniaApp.room.jail_restroom.message)


@bp.route('/airforce', methods=('GET', 'POST'))
def airforce_room():

    if request.method == 'POST':
        answer = request.form['answer']

        if answer == "A":

            return redirect(url_for('game.airforce_base'))

        elif answer == "B":

            return redirect(url_for('game.office_room'))


        else:

            return redirect(url_for('game.airforce_room'))

    return render_template('game/room.html', title=ww2maniaApp.room.airforce.name, message=ww2maniaApp.room.airforce.message)


@bp.route('/army', methods=('GET', 'POST'))
def army_room():

    if request.method == 'POST':
        answer = request.form['answer']

        if answer == "A":
            return redirect(url_for('game.push_up'))
        elif answer == "B":
            return redirect(url_for('game.army_train'))
        elif answer == "C":
            return redirect(url_for('game.office_room'))
        else:
            return redirect(url_for('game.army_room'))

    return render_template('game/room.html', title=ww2maniaApp.room.army.name, message=ww2maniaApp.room.army.message)


@bp.route('/navy', methods=('GET', 'POST'))
def navy_room():

    if request.method == 'POST':
        answer = request.form['answer']

        if answer == "A":
            return redirect(url_for('game.navy_deploy'))
        elif answer == "B":
            return redirect(url_for('game.office_room'))
        else:
            return redirect(url_for('game.navy_room'))

    return render_template('game/room.html', title=ww2maniaApp.room.navy.name, message=ww2maniaApp.room.navy.message)


@bp.route('/navyDeploy', methods=('GET', 'POST'))
def navy_deploy():

    if request.method == 'POST':
        answer = request.form['answer']

        if answer == 'A':
            return redirect(url_for('game.game_end'))

        elif answer == 'B':
            return redirect(url_for('game.jail_room'))

        else:
            return redirect(url_for('game.navy_deploy'))

    return render_template('game/room.html', title=ww2maniaApp.room.navy_deploy.name, message=ww2maniaApp.room.navy_deploy.message)

@bp.route('/pushUps', methods=('GET', 'POST'))
def push_up():
    """Do some push ups but then the end"""
    if request.method == 'POST':
        answer = request.form['answer']

        if answer == 'A':
            return redirect(url_for('game.game_end'))
        else:
            return redirect(url_for('game.push_up'))

    return render_template('game/room.html', title=ww2maniaApp.room.push_up.name, message=ww2maniaApp.room.push_up.message)

@bp.route('/armyTrain', methods=('GET', 'POST'))
def army_train():
    """Final army room then the end"""
    if request.method == 'POST':
        answer = request.form['answer']

        if answer == 'A':
            return redirect(url_for('game.game_end'))
        elif answer == 'B':
            return redirect(url_for('game.jail_room'))
        else:
            return redirect(url_for('game.army_train'))

    return render_template('game/room.html', title=ww2maniaApp.room.army_train.name, message=ww2maniaApp.room.army_train.message)


@bp.route('/airforceBase', methods=('GET', 'POST'))
def airforce_base():
    """Airforce last room then redirected to the ending. (Only choice)"""
    if request.method == 'POST':
        answer = request.form['answer']

        if answer == 'A':
            return redirect(url_for('game.game_end'))
        else:
            return redirect(url_for('game.airforce_base'))

    return render_template('game/room.html', title=ww2maniaApp.room.airforce_base.name, message=ww2maniaApp.room.airforce_base.message)


@bp.route('/game_ending', methods=('GET', 'POST'))
def game_end():

    return render_template('game/room.html', title=ww2maniaApp.room.good_game.name, message=ww2maniaApp.room.good_game.message)
