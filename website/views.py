# this is the file where all routes are made
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

# this single route is for the home page


@views.route('/')
def homepage():
    return render_template("home.html")
