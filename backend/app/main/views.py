from . import main
from flask import render_template,request,make_response,url_for,redirect

@main.route('/',methods=['GET'])
@main.route('/index',methods=['GET'])
def index():
    return render_template("index.html"),200