from . import admin
from flask import render_template,redirect,url_for,request

@admin.route('/',methods=['GET'])
def index():
    return render_template('cpanel-index.html')