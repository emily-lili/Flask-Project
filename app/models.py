from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(50))
    genre = db.Column(db.String(50), nullable=True, default='Unknown')
    rating = db.Column(db.String(50), nullable=True, default='Unknown')
    year = db.Column(db.Integer, nullable=True, default='Unknown')
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Character: {self.name}>"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
    def __repr__(self):
        return f"<User: {self.username}>"



