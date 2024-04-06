from . import api
from .wa import getWALink
from datetime import datetime
from flask import redirect, render_template
from app.models import db, Link, Product, Dates

@api.route('/ig/<token>', methods=['GET'])
def igLink(token):
 link = Link.query.filter_by(ig_link=token).first()
 if link:
    product = Product.query.filter_by(id=link.id_product).first()
    now = datetime.now()
    fnow = now.strftime("%d-%m-%Y")
    date = Dates(date=fnow,platform='ig',id_link=link.id)
    waLink = getWALink(link.no_wa, product.title)
    igClick = link.ig_click
    link.ig_click = igClick + 1
    db.session.merge(link)
    db.session.add(date)
    db.session.commit()
    return redirect(waLink)
 else:
   return render_template('404.html')