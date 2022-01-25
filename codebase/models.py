from enum import unique
from tkinter.tix import Tree
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000), unique = True)
    password = db.Column(db.String(100))
    