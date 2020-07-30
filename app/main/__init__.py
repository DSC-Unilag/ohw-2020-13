from flask import Blueprint

main = Blueprint(name='main',__name__)

from . import views
