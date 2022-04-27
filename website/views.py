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


@views.route('/product')
@login_required
def product():
    return render_template("home/product.html", user=current_user)


@views.route('/cake')
@login_required
def cake():
    return render_template("home/cake.html", user=current_user)


@views.route('/service')
@login_required
def service():
    return render_template("home/service.html", user=current_user)
