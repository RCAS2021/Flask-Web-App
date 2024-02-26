# Store standard routes for user authentication

# A blueprint has urls defined, it is a way to separate app, views can be defined in multiple files, 
# render_template renders the html templates,
# request works with HTTP request,
# flash flashes a message
# redirect is used to redirect to an url_for
from flask import Blueprint, render_template, request, flash, redirect, url_for
# Importing User
from .models import User
# Importing database
from . import db
# Importing from flask login to enable password hashing
from werkzeug.security import generate_password_hash, check_password_hash

# Define the auth blueprint
auth = Blueprint("auth", __name__)

# Creating routes for login, logout and sign_up
# Methods adds the methods listed so the route can accept it, making it able to receive those methods
@auth.route("/login", methods=["GET", "POST"])
def login():
    # Renders the template, can pass variables and therefore values
    return render_template("login.html", text="Testing", user="Pudha", boolean=True)

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # Get informations from the request
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # Restrictions and rules for adding user to database
        # Email too short
        if len(email) < 4:
            flash("Email must be longer than 3 characters", category="error")
        # First name too short
        elif len(first_name) < 2:
            flash("First name must be longer than 1 character", category="error")
        # Passwords don't match
        elif password1 != password2:
            flash("Passwords don\'t match", category="error")
        # Password too short
        elif len(password1) < 7:
            flash("Password must be longer than 6 characters", category="error")
        else:
            # Defining user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method="scrypt"))
            # Add new user to database
            db.session.add(new_user)
            # Make the commit to the database
            db.session.commit()
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("sign_up.html")
