from flask import Flask

from project import users
from project.settings import ProdConfig


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.run(debug=config_object.ENV == 'dev')

    print('Environment: ', config_object.ENV)

    register_blueprints(app)

    return app


def register_blueprints(app):
    """Register Flask blueprints."""

    app.register_blueprint(users.routes.app)
