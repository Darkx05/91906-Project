# imports
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

# the route below allows home to run


@views.route('/')
# this is for the home page as it will
# show only when logged in
@login_required
def home():
    return render_template("home.html", user=current_user)
