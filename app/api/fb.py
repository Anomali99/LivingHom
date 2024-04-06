from . import api
from .wa import getWALink
from flask import redirect, render_template
from app.models import db, Link, Product

@api.route('/fb/<token>', methods=['GET'])
def fbLink(token):
 link = Link.query.filter_by(fb_link=token).first()
 if link:
    product = Product.query.filter_by(id=link.id_product).first()
    waLink = getWALink(link.no_wa, product.title)
    fbClick = link.fb_click
    link.fb_click = fbClick + 1
    db.session.merge(link)
    db.session.commit()
    return redirect(waLink)
 else:
   return render_template('404.html')