from enum import unique
from tkinter.tix import Tree
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000), unique = True)
    password = db.Column(db.String(100))
    