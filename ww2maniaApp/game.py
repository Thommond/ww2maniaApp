import functools
from flask import (  # Tools for later
    Blueprint, Flask, g, redirect, render_template, request, session, url_for
)
import ww2maniaApp.items  # gives info on the items the player uses like a gas_mask

import ww2maniaApp.char  # gives more info on char stats/ health / name

import ww2maniaApp.room  # Imports each rooms message/ descripton so then the
# info can be routed to the proper template page

# This is a blueprint of the game function so all template that
# relate to the game are routed here / makes code more DRY
bp = Blueprint('game', __name__, url_prefix='/game')


@bp.route('/')  # The menu function will be the root route of
# the project
def menu():
    # Choose info about game or to play game
    return render_template('base.html')

# The how to play function is to inform players
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
        # Needs to be made
        # if answer == "A":
        #     return redirect(url_for('game.army'))
        # elif answer == "B":
        #     return redirect(url_for('game.navy'))
        # elif anwser == "C":
        #     return redirect(url_for('game.airforce'))
        # else:
        #     return redirect(url_for('game.office'))

    return render_template('game/room.html', title=ww2maniaApp.room.office.name, message=ww2maniaApp.room.office.message)

# Jail is a game if you choose to go to jail in the first answer you make
@bp.route('/jail', methods=('GET', 'POST'))
def jail_room():

    if request.method == 'POST':
        answer = request.form['answer']

        # if answer == "A":
        #     return redirect(url_for('game.jail_yard'))  # Needs to be created
        # elif answer == "B":
        #     return redirect(url_for('game.jail_locker'))  # Needs to be created
        #
        # elif answer == "C":
        #     return redirect(url_for('game.jail_house')) # Needs to be created
        # else:
        #     return redirect(url_for('game.jail_room'))  # if they do not supply

    return render_template('game/room.html', title=ww2maniaApp.room.jail.name, message=ww2maniaApp.room.jail.message)
