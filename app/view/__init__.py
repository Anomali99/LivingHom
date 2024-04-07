from flask import Blueprint

view = Blueprint('view',__name__)

from . import home
from . import product
from . import users
from . import chart