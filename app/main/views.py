from . import main
from flask import render_template,redirect,flash,url_for,request,make_response,session
from flask import current_app as app
from app.extensions import db,bcrypt
from models import Admin
from sqlalchemy.exc import IntegrityError
from functools import wraps
import datetime as d


@main.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        password = bcrypt.generate_password_hash(request.form['password'])
        new_admin = Admin(first_name=request.form['firstName'],last_name=request.form['lastName'],email=request.form['email'],password=password)
        try:
            db.session.flush(objects=[new_admin])
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            error = 'User Already Exists'
            return render_template('signup.html',msg=error),400
    elif request.method == 'GET':
        return render_template('signup.html'),200

@main.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # fetch login details
        email = request.form['email']
        password = request.form['password']
        # find user with matching email
        user = Admin.query.filter_by(email=email).first()
        if not user:
            flash(u"No such user found",'error')
            return render_template('login.html'),404
        else:
            if bcrypt.check_password_hash(user.password,password):
                session.permanent = True
                session['admin_id'] = user.admin_id
                return redirect(url_for('main.dashboard')),200
            flash(u'Incorrect Password','error')
            return render_template('login.html'),400


# Authorization decorator
def login_required(f):
    @wraps(f)
    def function(*args,**kwargs):
        admin_id = None
        if admin_id in session:
            admin_id = session['admin_id']
            # find admin with matching ID
            user = Admin.query.filter_by(admin_id=admin_id).first()
            if user:
                return f(user,*args,**kwargs)
            else:
                flash(u'Invalid Login credentials','error')
                return redirect(url_for('main.login')),401
        else:
            flash(u'You\'re not logged in','error')
            return redirect(url_for('main.login')),401
        
    return function

@main.route('/dashboard',methods=['POST','GET'])
@login_required
def dashboard():
    pass
    