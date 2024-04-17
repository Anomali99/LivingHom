from . import api
from .wa import getWALink
from datetime import datetime
from flask import redirect, render_template
from app.models import db, Link, Product, Dates
import random

@api.route('/web/<token>', methods=['GET'])
def webLink(token):
 link = Link.query.filter_by(web_link=token).first()
 if link:
    product = Product.query.filter_by(id=link.id_product).first()
    now = datetime.now()
    fnow = now.strftime("%d-%m-%Y")
    date = Dates(date=fnow,platform='web',id_link=link.id)
    waLink = getWALink(link.no_wa, product.title)
    webClick = link.web_click
    link.web_click = webClick + 1
    db.session.merge(link)
    db.session.add(date)
    db.session.commit()
    return redirect(waLink)
 else:
   return render_template('404.html')
 
@api.route('/dummy')
def dummy():
   products = Product.query.all()
   total_clicks = 50
   start_date = [f'{tgl}-04-2024' for tgl in ['05','07','08','11','15']]

   click_count = 0
   while  click_count < total_clicks :
      generate = ''.join(random.choices('01234567', k=1)) 
      product = products[int(generate)]
      link = Link.query.filter_by(id_product=product.id).first()
      if link:
         rTgl = ''.join(random.choices('01234', k=1))
         date_str = start_date[int(rTgl)]
         gen = ''.join(random.choices('123', k=1)) 
         platform = ''
         if gen == '1':
            platform = 'web'
            webClick = link.web_click
            link.web_click = webClick + 1
         elif gen == '2':
            platform = 'fb'
            fbClick = link.fb_click
            link.fb_click = fbClick + 1
         elif gen == '3':
            platform = 'ig'
            igClick = link.ig_click
            link.ig_click = igClick + 1
         date = Dates(date=date_str,platform=platform,id_link=link.id)
         db.session.merge(link)
         db.session.add(date)
      click_count += 1
   db.session.commit()
   return 'ok'

@api.route('/remove')
def remove():
   links = Link.query.all()
   for link in links:
      link.web_click = 0
      link.ig_click = 0
      link.fb_click = 0
      db.session.merge(link)
   dates = Dates.query.all()
   for date in dates:
      db.session.delete(date) 
   db.session.commit()
   return 'ok'
