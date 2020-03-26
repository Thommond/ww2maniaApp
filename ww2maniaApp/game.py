import functools
from flask import (
    Blueprint, Flask, g, redirect, render_template, request, session, url_for
)

import ww2maniaApp.room


bp = Blueprint('game', __name__, url_prefix='/game')


@bp.route('/')
def menu():

    return render_template('base.html')


@bp.route('/howtoplay', methods=('GET', 'POST'))
def howtoplay():

    return render_template('game/howToPlay.html')


@bp.route('/welcome', methods=('GET', 'POST'))
def welcome():

    if request.method == 'POST':
        answer = request.form['answer']

        if answer == "A":
            return redirect(url_for('game.office_room'))
        elif answer == "B":
            return redirect(url_for('game.jail_room'))

    return render_template('game/room.html', title=ww2maniaApp.room.welcome.name, message=ww2maniaApp.room.welcome.message)


@bp.route('/dead', methods=('GET', 'POST'))
def dead_room():
    return render_template('game/room.html', title=ww2maniaapp.room.dead.name, message=ww2maniaApp.room.dead.message)


@bp.route('/office', methods=('GET', 'POST'))
def office_room():
    return render_template('game/room.html', title=ww2maniaApp.room.office.name, message=ww2maniaApp.room.office.message)


@bp.route('/jail', methods=('GET', 'POST'))
def jail_room():
    return render_template('game/room.html', title=ww2maniaApp.room.jail.name, message=ww2maniaApp.room.jail.message)
