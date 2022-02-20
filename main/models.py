from flask_login import UserMixin
from . import db, bodovani

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000), unique = True)
    password = db.Column(db.String(100))

class Body(bodovani.Model):
    id = bodovani.Column(bodovani.Integer, primary_key=True)
    username = bodovani.Column(bodovani.String(1000), unique = False)
    odpoved_1 = bodovani.Column(bodovani.String(1000), unique = False)
    odpoved_2 = bodovani.Column(bodovani.String(1000), unique = False)
    odpoved_3 = bodovani.Column(bodovani.String(1000), unique = False)