import functools
from flask import (
    Blueprint, Flask, g, redirect, render_template, request, session, url_for
)


class Room(object):
    """docstring for Rooms ."""

    def __init__(self, name):
        self.name = name


bp = Blueprint('game', __name__)


@bp.route('/')
def menu():

    return render_template('base.html')


@bp.route('/howtoplay', methods=('GET', 'POST'))
def howtoplay():

    return render_template('game/howToPlay.html')


@bp.route('/welcome', methods=('GET', 'POST'))
def welcome():

    return render_template('game/room.html')


@bp.route('/dead', methods=('GET', 'POST'))
def dead():
    return render_template('game/dead')
