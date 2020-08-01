from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from .main import main
from .admin import admin

def create_app(config_name):
    app = Flask(__name__)

    # config app
    app.config.from_object(config[str(config_name)])

    # register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(admin,url_prefix='/admin')

    return app
