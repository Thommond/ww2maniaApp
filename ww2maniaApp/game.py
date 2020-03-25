import functools
from flask import (
    Blueprint, Flask, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('game', __name__, url_prefix='/game')


@bp.route('/menu', methods=('GET', 'POST'))
def menu():

    return render_template('/game/menu.html')


@bp.route('/howtoplay', methods=('GET', 'POST'))
def howtoplay():

    return render_template('/game/howToPlay.html')


@bp.route('/room1', methods=('GET', 'POST'))
def roomone():

    return render_template('/game/room1.html')


@bp.route('/room2', methods=('GET', 'POST'))
def roomtwo():

    return render_template('/game/room2.html')
