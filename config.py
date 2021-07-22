import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
        Set config variables for our flask app
        Using environmental variables where necessary
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or "you will never guess my key"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    #if os.environ.get('DATABASE_URL').startswith('postgres'):
        #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # stop tracking database changes through sqlalchemy