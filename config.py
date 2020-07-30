import os

basedir = os.getcwd()

class Config:
    """
        Base config class, contains config that are generic to all other 
        sub-config classes for various purposes
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/ohw13Dev.sqlite"
    FLASK_ENV='development'
    DEBUG=True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/ohw13Test.sqlite"
    FLASK_ENV='testing'
    DEBUG=True

class ProductionConfig(Config):
    SQALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') # Heroku Demands this
    FLASK_ENV='production'
    DEBUG=True

config = {
    "default":DevelopmentConfig,
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig
}
