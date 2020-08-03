from app import create_app,db
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app = create_app('default' or os.getenv('FLASK_CONFIG'))
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_contex():
    return dict(app=app,db=db,migrate=migrate)

