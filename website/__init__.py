from flask import Flask
# Importing SQLAlchemy for the database
from flask_sqlalchemy import SQLAlchemy
# Importing path module
from os import path
# Importing LoginManager
from flask_login import LoginManager

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
    from .models import User, Note

    # New mode to create database
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    # Where should flask redirect if user not logged in
    login_manager.login_view = "auth.login"
    # Tell which app is being used
    login_manager.init_app(app)

    # Telling Flask how to load the user, referencing the user by id
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
