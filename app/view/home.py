from . import view
from datetime import datetime
from app.models import Product, Images
from flask import render_template, session, redirect, jsonify

@view.route('/', methods=['GET'])
def home():
    login = session.get('login')
    if login:
        time = session.get('time')
        current = datetime.now().strftime('%Y-%m-%d')
        if time != current:
            return redirect('/logout', methods=['GET'])
    products = Product.query.outerjoin(Images).all()
    return render_template('home.html', login=login, products=products)
    