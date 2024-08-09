from flask import Blueprint

bp = Blueprint('chat', __name__)

from flaskapp.chat import routes