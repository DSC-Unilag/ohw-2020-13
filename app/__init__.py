from flask import Flask
from .extensions import db,migrate
from .cpanel import cpanel
from .main import main
from config import config

# App Factory
def __call__(config_name):
    app = Flask (__name__)

    # Add config from config.py
    app.config.from_object(config[çonfig_name])

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(cpanel,url_prefix='/cpanel') # our admin panel, not the one for NGOs
    app.register_blueprint(main) # all site-buidling related requests go here
    return app