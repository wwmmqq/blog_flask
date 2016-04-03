# -*- coding: utf-8 -*-
'''blog __init__
'''

from flask import Blueprint

blog = Blueprint('blog', __name__, url_prefix='/blog',template_folder='templates', static_folder='static')

from . import views
