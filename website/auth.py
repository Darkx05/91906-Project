from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

# routes/pathways
# brackets after auth route is required to move around the site
# if users are to move manually


@auth.route('/login', method=['GET, POST'])
def login_page():
    data = request.form()
    print(data)
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up', method=['GET, POST'])
def signup():
    # user handling on post requests
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            # adds user info to database
            pass
    return render_template("sign_up.html")

            pass
        elif len(password1) < 7:
            pass
        else:
            # adds user info to database
            pass
    return render_template("sign_up.html")
