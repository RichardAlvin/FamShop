from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def market():
    return render_template("home.html")
