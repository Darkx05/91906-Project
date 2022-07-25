from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

# routes/pathways
# brackets after auth route is required to move around the site
# if users are to move manually


@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    email = request.form.get('email')
    password = request.form.get('password')

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

        if len(email) < 4:
            flash('Email must be greater than 4 characters!', category='try again')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character!', category='try again')
        elif password1 != password2:
            flash('Passwords don\'t match!', category='try again')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters!', category='try again')
        else:
            # adds user info to database
            flash('Details saved', category='success.')
    return render_template("sign_up.html")

@auth.route('/about')
def about():
    return render_template("about.html")
