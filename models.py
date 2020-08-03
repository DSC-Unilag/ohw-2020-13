#from run import db
from app import db

class Admin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(200),unique=True)
    password = db.Column(db.String(100))
    admin_id = db.Column(db.String(200),unique=True)
    site_data = db.relationship('Config',backref='ngo-admin',uselist=False)

class Config(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    site_name = db.Column(db.String(100)) #Ngo name or something else
    logo = db.Column(db.String(200)) #url to image
    admin_id = db.Column(db.Integer,db.ForeignKey('admin.id'))
    content = db.relationship('Content',backref='config')

class Content(db.Model):
    id = db.Column(db.Integer,primary_key=True)

    ## content goes here

    config_id = db.Column(db.Integer,db.ForeignKey('config.id'))

    