# Store standard routes for user navigation

# A blueprint has urls defined, way to separate app, views can be defined in multiple files to better organize
from flask import Blueprint, render_template

# Define the views blueprint (views = blueprint name)
views = Blueprint("views", __name__)

# Main page: /
# @ -> Decorator
@views.route("/")
def home():
    # Renders the template, can pass variables and therefore values
    return render_template("home.html")
