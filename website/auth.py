# Store standard routes for user authentication

# A blueprint has urls defined, way to separate app, views can be defined in multiple files
from flask import Blueprint, render_template

# Define the auth blueprint
auth = Blueprint("auth", __name__)

# Creating routes for login, logout and sign_up
@auth.route("/login")
def login():
    # Renders the template, can pass variables and therefore values
    return render_template("login.html", text="Testing", user="Pudha", boolean=True)

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")
