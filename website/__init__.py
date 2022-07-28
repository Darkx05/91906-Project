# modules imported
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
# database setup
db = SQLAlchemy()
DB_NAME = "database.db"
# all functions go here


def app_creation():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'string'
    # this stores the database in the website folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # these signify the different routes from the view file
    db.init_app(app)
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    database_create(app)

    from .models import User, Note
    return app

def database_create(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
