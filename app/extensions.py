"""
:Extensions are instantiated here and instances imported in the
dunder init file for the app,to be initiated with the appp factory
function

"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

