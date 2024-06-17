from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def initialize_extensions(app: Flask):
    db.init_app(app)
