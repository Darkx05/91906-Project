from flask import Blueprint, render_template
from templates import base
auth = Blueprint('auth', __name__)

# routes/pathways
# brackets after auth route is required to move around the site
# if users are to move manually


@auth.route('/login')
def login_page():
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up')
def signup():
    return render_template("sign_up.html")

