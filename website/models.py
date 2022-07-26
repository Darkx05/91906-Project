from . import db 
from flask_login import UserMixin
# this class is for the columns for a database layout

class User(db.Model, UserMixin):
    id = db.column(db.Integer, primary_key=True)
