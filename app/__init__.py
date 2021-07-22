from flask import Flask
from config import Config

from .site.routes import site 
from .authentication.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db

app = Flask(__name__) 

app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app,db)


from . import models
