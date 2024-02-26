from flask import Flask

def create_app():
    # Initialize flask
    app = Flask(__name__)

    # Secure the cookies and session data related to the website - provisory key for development, never share in production
    app.config["SECRET_KEY"] = 'provisory key for development, never share in production'

    return app