from flask import Blueprint

bp = Blueprint('store', __name__)

from flaskapp.store import routes
