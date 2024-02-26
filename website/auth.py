# Store standard routes for user navigation

# A blueprint has urls defined, way to separate app, views can be defined in multiple files
from flask import Blueprint

# Define the auth blueprint
auth = Blueprint("auth", __name__)

# Creating routes for login, logout and sign_up
@auth.route("/login")
def login():
    return "<p>Login</p>"

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up")
def sign_up():
    return "<p>Sign Up</p>"
