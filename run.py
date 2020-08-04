from app import __call__
from app.extensions import db
from flask_migrate import Migrate
import os

app = __call__(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_contex():
    return dict(app=app,db=db,migrate=migrate)

