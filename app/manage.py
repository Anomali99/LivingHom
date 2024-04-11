from flask import Flask
from .config import Config
from .models import db
from .api import api
from .view import view
import matplotlib

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api)
app.register_blueprint(view)
db.init_app(app)
matplotlib.use('Agg')

with app.app_context():
    db.create_all()
