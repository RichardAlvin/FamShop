from pytz import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    favorite = db.relationship('Favorite')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150), unique=True)
    product_desc = db.Column(db.String())
    product_pict = db.Column(db.String())
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    favorite = db.relationship('Favorite')


# class Product():
