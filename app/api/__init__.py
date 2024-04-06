from flask import Blueprint

api = Blueprint('api',__name__)

from . import fb
from . import ig
from . import web
from . import wa