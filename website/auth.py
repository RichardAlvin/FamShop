from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("auth/login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(fname) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif password != cpassword:
            flash('Password dont match.', category='error')
        elif len(password) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        else:
            flash('Account Created!', category='success')
            # add user to database

    return render_template("auth/sign_up.html")
