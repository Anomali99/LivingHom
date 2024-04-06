from . import api
from .wa import getWALink
from flask import redirect, render_template
from app.models import db, Link, Product

@api.route('/web/<token>', methods=['GET'])
def webLink(token):
 link = Link.query.filter_by(web_link=token).first()
 if link:
    product = Product.query.filter_by(id=link.id_product).first()
    waLink = getWALink(link.no_wa, product.title)
    webClick = link.web_click
    link.web_click = webClick + 1
    db.session.merge(link)
    db.session.commit()
    return redirect(waLink)
 else:
   return render_template('404-link-notfound.html')