from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # simple test app

    @app.route('/Demo')
    def index():
        return 'Flask Heroku Demo'
    # TO DO database
    # from . import db
    # db.init_app(app)

    from . import game
    app.register_blueprint(game.bp)

    # TO DO THURS (Make DB and cookies to save Data)

    # from . import auth
    # app.register_blueprint(auth.bp)
    #
    # from . import items
    # app.register_blueprint(items.bp)
    #
    # from . import stats
    # app.register_blueprint(stats.bp)

    app.add_url_rule('/', endpoint='menu')
    return app
