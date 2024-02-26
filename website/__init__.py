from flask import Flask
# Importing SQLAlchemy for the database
from flask_sqlalchemy import SQLAlchemy
# Importing path module
from os import path

# Initializing database, imported on models
db = SQLAlchemy()
# Choosing database name
DB_NAME = "database.db"

def create_app():
    # Initialize flask
    app = Flask(__name__)
    # Secure the cookies and session data related to the website - provisory key for development, never share in production
    app.config["SECRET_KEY"] = 'provisory key for development, never share in production'
    # Telling the flask app that we are using an database and where using sqlite3
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    # Initialize the database giving the app
    db.init_app(app)

    # import the blueprints
    from .views import views
    from .auth import auth

    # Register the blueprints on flask app
    # Prefix - for example, if you create a view with route hello, and the url_prefix is /auth/, it would be needed to go to /auth/hello, using only /, it goes to /hello
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Importing user and note to make sure to load the file before creating the database
    from . import models

    create_database(app)

    return app

def create_database(app):
    # Check if database exists
    if not path.exists("website/" + DB_NAME):
        # pylint: disable-next=E1123
        db.create_all(app=app)
        print("Created Database!")
