from flask import Flask
from .extensions import db,migrate
from .cpanel import cpanel
from .main import main

# App Factory
def __call__():
    app = Flask (__name__)

    db.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(cpanel,url_prefix='/cpanel') # our admin panel, not the one for NGOs
    app.register_blueprint(main) # all site-buidling related requests go here
    return app