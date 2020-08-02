from flask import Flask
from .extensions import db,bcrypt
from config import config

def __call__(config_name):
    app = Flask(__name__)

    bcrypt.init_app(app)
    db.init_app(app)

    # config app
    app.config.from_object(config[config_name])

    # register Blueprints
    from .main import main
    from .admin import admin

    app.register_blueprint(main)
    app.register_blueprint(admin,url_prefix='/admin')

    return app
