from flask import Blueprint

cpanel = Blueprint(name='cpanel',__name__)

from . import views