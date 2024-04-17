from . import view
from datetime import datetime
from app.models import db, Product, Images, Link, Comment
from flask import render_template, session, redirect, request
import socket

@view.route('/', methods=['GET', 'POST'])
def home():
    login = session.get('login')
    if login:
        time = session.get('time')
        current = datetime.now().strftime('%Y-%m-%d')
        if time != current:
            return redirect('/logout')
    products = Product.query.outerjoin(Images).all()
    return render_template('home.html', login=login, products=products)
    
@view.route('/detail/<id>', methods=['GET', 'POST'])
def detail(id):
    login = session.get('login')
    if login:
        time = session.get('time')
        current = datetime.now().strftime('%Y-%m-%d')
        if time != current:
            return redirect('/logout')
    product = Product.query.filter_by(id=id).outerjoin(Images).first()
    if product:
        link = Link.query.filter_by(id_product=product.id).first()
        comments = Comment.query.filter_by(id_product=product.id).all()
        IPaddress = socket.gethostbyname(socket.gethostname())
        URI = f'http://{IPaddress}:5127' 
        if request.method == 'POST':
            type = request.form['form_type']
            if type == 'addComment':
                nama = request.form['name']
                comment = request.form['comment']
                newComment = Comment(name=nama,comment=comment,id_product=product.id)
                db.session.add(newComment)
                db.session.commit()
            elif type == 'update':
                title = request.form['title']
                price = request.form['price']
                description = request.form['description']
                wa = request.form['wa']
                webCheckout = request.form['webCheckout']
                igCheckout = request.form['igCheckout']
                fbCheckout = request.form['fbCheckout']
                newProduct = product
                newLink = link
                newProduct.title = title
                newProduct.price = price
                newProduct.description = description
                newLink.wa = wa
                newLink.web_checkout = webCheckout
                newLink.ig_checkout = igCheckout
                newLink.fb_checkout = fbCheckout
                db.session.merge(newProduct)
                db.session.merge(newLink)
                db.session.commit()
        return render_template('detail.html', login=login, product=product, link=link, comments=comments, IPserver=URI)
    else:
        return render_template('404.html')
