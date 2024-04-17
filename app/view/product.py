from . import view
from datetime import datetime
from app.models import db, Product, Images, Link
from flask import render_template, session, request, redirect, current_app
from .chart import getChartAll, getChartCustomAll, getChartWeek, getChartYear, getChartMonth, getChartProduct, getChartMonthAll, getChartWeekAll, getChartYearAll
import os
import socket
import random

@view.route('/product', methods=['GET','POST'])
def product():
    login = session.get('login')
    if login:
        time = session.get('time')
        current = datetime.now().strftime('%Y-%m-%d')
        if time != current:
            return redirect('/logout')
    else:
        return redirect('/')
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

@view.route('/monitoring', methods=['GET','POST'])
def monitoring():
    login = session.get('login')
    if login:
        time = session.get('time')
        current = datetime.now().strftime('%Y-%m-%d')
        if time != current:
            return redirect('/logout')
    else:
        return redirect('/')
    if request.method == 'POST':
        menu = request.form['cbx-chart']
        if menu == '9':
            date1 = request.form['date1']
            date2 = request.form['date2']
            getChartCustomAll(date1=date1, date2=date2, title=None)
        elif menu == '3':
            getChartWeekAll()
        elif menu == '4':
            getChartMonthAll()
        elif menu == '5':
            getChartYearAll()
        elif menu == '2':
            idProduct = request.form['id_product']
            getChartProduct(id=idProduct)
        elif menu == '6':
            idProduct = request.form['id_product']
            getChartWeek(id=idProduct)
        elif menu == '7':
            idProduct = request.form['id_product']
            getChartMonth(id=idProduct)
        elif menu == '8':
            idProduct = request.form['id_product']
            getChartYear(id=idProduct)
        else:
            getChartAll()
    else:
        getChartAll()
    products = Product.query.all()
    IPaddress = socket.gethostbyname(socket.gethostname())
    URI = f'http://{IPaddress}:5127' 
    return render_template('monitoring.html', login=login, products=products, IPserver=URI)