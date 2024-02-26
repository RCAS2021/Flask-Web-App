from flask import Flask

def create_app():
    # Initialize flask
    app = Flask(__name__)
    # Secure the cookies and session data related to the website - provisory key for development, never share in production
    app.config["SECRET_KEY"] = 'provisory key for development, never share in production'

    # import the blueprints
    from .views import views
    from .auth import auth

    # Register the blueprints on flask app
    # Prefix - for example, if you create a view with route hello, and the url_prefix is /auth/, it would be needed to go to /auth/hello, using only /, it goes to /hello
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
