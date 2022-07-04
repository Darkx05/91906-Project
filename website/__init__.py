# modules imported
from flask import Flask

# all functions go here


def app_creation():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'string'
    # these signify the different routes from the view file
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
