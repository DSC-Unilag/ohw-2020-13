from flask import Flask
from .extensions import db,migrate

# App Factory
def __call__():
    app = Flask (__name__)

    db.init_app(app)
    migrate.init_app(app)

    app.register_blueprint()
    app.register_blueprint()
    return app