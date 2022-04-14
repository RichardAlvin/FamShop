from flask import Blueprint, render_template
from flask_login import login_required, current_user
from sqlalchemy import null

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home/home.html", user=current_user)


@views.route('/shop')
@login_required
def shop():
    return render_template("home/home.html", user=current_user)
