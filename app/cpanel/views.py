from . import cpanel
from flask import render_template,request,make_response,url_for,redirect

@cpanel.route('/',methods=['GET'])
@cpanel.route('/index',methods=['GET'])
def index():
    return render_template("cpanel-index.html"),200
