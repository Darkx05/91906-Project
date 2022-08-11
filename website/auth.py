# imports
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note
import json
auth = Blueprint('auth', __name__)

# auth login page route


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # variables required
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        # if user tries to sign up when an account is existing
        # this message appears
        if user:
            flash('Email already exists.', category='error')
        # exception handling in form
        elif len(email) < 4:
            flash('Sorry, that is invalid!', category='error')
        elif len(first_name) < 2:
            flash('Sorry, that is invalid!', category='error')
        elif password1 != password2:
            flash('Sorry, they need to match!', category='error')
        elif len(password1) < 7:
            flash('Sorry, that is invalid!', category='error')
        else:
            new_user = User(email=email, first_name=first_name, 
            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

# route for the about page


@auth.route('/about', methods=['GET', 'POST'])
@login_required
def about():
    if request.method == 'POST':
        note = request.form.get('note')
        # exception handling that text must be
        # entered in order for notes to work
        if len(note) < 1:
            flash('You put nothing! try again!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            # message shown when a note is added
            flash('Note added!', category='success')

    return render_template("about.html", user=current_user)


@auth.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})



# route for support page


@auth.route('/support')
def support():
    return render_template("support.html", user=current_user)
