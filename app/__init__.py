from flask import Flask


# App Factory
def __call__():
    app = Flask (__name__)

    app.register_blueprint()
    app.register_blueprint()
    return app