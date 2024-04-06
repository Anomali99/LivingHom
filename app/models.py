from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    images = db.relationship('Images', backref='product', lazy=True)
    comment = db.relationship('Comment', backref='product', lazy=True)
    link = db.relationship('Link', backref='product', lazy=True)

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    image_uri = db.Column(db.String, nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    nama = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    no_wa = db.Column(db.String, nullable=False)
    web_link = db.Column(db.String, nullable=False)
    fb_link = db.Column(db.String, nullable=False)
    ig_link = db.Column(db.String, nullable=False)
    web_click = db.Column(db.Integer, nullable=False, default=0)
    fb_click = db.Column(db.Integer, nullable=False, default=0)
    ig_click = db.Column(db.Integer, nullable=False, default=0)
    web_checkout = db.Column(db.Integer, nullable=False, default=0)
    ig_checkout = db.Column(db.Integer, nullable=False, default=0)
    fb_checkout = db.Column(db.Integer, nullable=False, default=0)

def insert_default_user(*args, **kwargs):
    if User.query.count() == 0:
        default_user = User(username='admin', password=generate_password_hash('123'))
        db.session.add(default_user)
        db.session.commit()
event.listen(User.__table__, 'after_create', insert_default_user)
