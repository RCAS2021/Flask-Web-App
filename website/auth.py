# Store standard routes for user authentication
# Importing User
from .models import User
# Importing database
from . import db
# A blueprint has urls defined, it is a way to separate app, views can be defined in multiple files, 
# render_template renders the html templates,
# request works with HTTP request,
# flash flashes a message
# redirect is used to redirect to an url_for
from flask import Blueprint, render_template, request, flash, redirect, url_for
# Importing from flask login to enable password hashing
from werkzeug.security import generate_password_hash, check_password_hash
# Importing flask login_user, login_required, logout_user, current_user
from flask_login import login_user, login_required, logout_user, current_user

# Define the auth blueprint
auth = Blueprint("auth", __name__)

# Creating routes for login, logout and sign_up
# Methods adds the methods listed so the route can accept it, making it able to receive those methods
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Getting the entered information
        email = request.form.get("email")
        password = request.form.get("password")

        # Queries to encounter the first email match
        user = User.query.filter_by(email=email).first()
        # If user email was encountered
        if user:
            # Check if the user password equal to the password entered
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                # Login user
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")

    # Renders the template, can pass variables and therefore values
    return render_template("login.html", user=current_user)

@auth.route("/logout")
# Makes sure that this page cannot be accessed if not logged in
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # Get informations from the request
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # Restrictions and rules for adding user to database
        # Checking if user already exists
        # Queries to encounter the first email match
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category="error")
        # Email too short
        elif len(email) < 4:
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
            # Log in user
            login_user(new_user, remember=False)
            flash("Account created!", category="success")
            # Redirects to the mapped url
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user)
