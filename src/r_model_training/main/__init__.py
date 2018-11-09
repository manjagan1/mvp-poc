from flask import Flask
from .config import config_by_name


def create_app(app_mode):
    app = Flask(__name__)
    app.config.from_object(config_by_name[app_mode])

    return app
