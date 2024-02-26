# CREATING DATABASE MODULES
# Helps logging users
from flask_login import UserMixin
# Enables sqlalchemy to automatically add the date time using now
from sqlalchemy.sql import func
# Import the database
from . import db

# Define the name of the object and have it inherit from db.Model
class Note(db.Model):
    # Creating Note schema
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    # Timezone = True keeps the timezone information
    # Disabling pylint func.now() not callable error message, false-positive
    # pylint: disable-next=E1102
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # On sql, user will be registered as user and not User even though the class is named User
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

# Define the name of the object and have it inherit from db.Model, just for the user, also inherit UserMixin
class User(db.Model, UserMixin):
    # Creating User schema
    # Creating primary key
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Makes so sqlalchemy creates the relationship, uses capitalized Note instead of note on this one
    notes = db.relationship("Note")
