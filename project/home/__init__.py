from flask import Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates', static_folder='static')

import datatable
import views