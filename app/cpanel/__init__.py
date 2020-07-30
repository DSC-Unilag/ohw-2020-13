from flask import Blueprint

cpanel = Blueprint('cpanel',__name__,template_folder='templates')

from . import views