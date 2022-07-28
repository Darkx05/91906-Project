# all imports are here
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# routes/pathways
# brackets after auth route is required to move around the site
# if users are to move manually


@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login Succsessful', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('wrong password, try again', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    # user handling on post requests
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        if len(email) < 4:
            flash('Sorry, that is invalid!', category='try again')
        elif len(firstName) < 2:
            flash('Sorry, that is invalid!', category='try again')
        elif password1 != password2:
            flash('Passwords don\'t match!', category='try again')
        elif len(password1) < 7:
            flash('Sorry, that is invalid', category='try again')
        else:
            # this part creates the account
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # adds user info to database
            flash('Details saved', category='Success!')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")

# route for the about page
@auth.route('/about')
def about():
    return render_template("about.html")
