from flask import Flask

from app.api import register_blueprints
from app.configs import config_dict
from app.extensions import initialize_extensions


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_dict.get(config_name, "prod"))

    initialize_extensions(app)
    register_blueprints(app)

    return app
