import os
basedir = os.getcwd()

class Config:
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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
