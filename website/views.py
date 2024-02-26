# Store standard routes for user navigation

# A blueprint has urls defined, way to separate app, views can be defined in multiple files
from flask import Blueprint

# Define the views blueprint
views = Blueprint("views", __name__)

# Main page: /
# @ -> Decorator
@views.route("/")
def home():
    return "<h1>Test</h1>"
