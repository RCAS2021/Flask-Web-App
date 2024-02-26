# Store standard routes for user navigation

# A blueprint has urls defined, way to separate app, views can be defined in multiple files to better organize
from flask import Blueprint, render_template
# Importing flask login_user, login_required, logout_user, current_user
from flask_login import login_required, current_user

# Define the views blueprint (views = blueprint name)
views = Blueprint("views", __name__)

# Main page: /
# @ -> Decorator
@views.route("/")
# Makes so you cannot get to the home page if not logged in
@login_required
def home():
    # Renders the template, can pass variables and therefore values
    return render_template("home.html")
