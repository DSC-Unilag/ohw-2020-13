import os
from datetime import timedelta
basedir = os.getcwd()

class Config:
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME= timedelta(minutes=30)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/devDb.db"
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    FLASK_ENV='production'

config = {
    "default":DevConfig,
    "development":DevConfig,
    "production":ProdConfig
}
