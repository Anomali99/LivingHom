from . import view
from datetime import datetime
from app.models import db, Product, Images, Link
from flask import render_template, session, request, redirect, current_app
import os
import random

@view.route('/product', methods=['GET','POST'])
def product():
    login = session.get('login')
    if login:
        time = session.get('time')
        current = datetime.now().strftime('%Y-%m-%d')
        if time != current:
            return redirect('/logout')
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        description = request.form['description']
        wa = request.form['wa']
        images = request.files.getlist('cover')
        product = Product(title=title, description=description, price=price)
        db.session.add(product)
        db.session.commit()
        index = 1
        for image in images:
            now = datetime.now().strftime("%y%m%d%H%M%S")
            filename = f"{now}{index}.{image.filename.rsplit('.',1)[1]}"
            index = index + 1
            newImage = Images(id_product=product.id, image_uri=filename)
            db.session.add(newImage)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(filepath)
        webLink = generateLink(product.id)
        igLink = generateLink(product.id)
        fbLink = generateLink(product.id)
        link = Link(id_product=product.id, no_wa=wa, web_link=webLink, fb_link=fbLink, ig_link=igLink)
        db.session.add(link)
        db.session.commit()
        return redirect(f'/detail/{product.id}')
    return render_template('product.html', login=login)

def generateLink(id) -> str:
    generate = ''.join(random.choices('0123456789', k=10))  
    return f'{generate}{str(id)}'