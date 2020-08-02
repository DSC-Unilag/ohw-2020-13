from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import config

bcrypt = Bcrypt()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    bcrypt.init_app(app)
    db.init_app(app)

    # config app
    app.config.from_object(config[str(config_name)])

    # register Blueprints
    from .main import main
    from .admin import admin
    
    app.register_blueprint(main)
    app.register_blueprint(admin,url_prefix='/admin')

    return app
