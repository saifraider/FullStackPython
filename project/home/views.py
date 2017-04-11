
from flask import render_template, Blueprint, \
    request, flash, redirect, url_for   # pragma: no cover
from flask.ext.login import login_required, current_user   # pragma: no cover

from project.home.message_form import MessageForm   # pragma: no cover
#from project import db   # pragma: no cover
#from project.models import BlogPost   # pragma: no cover

home_blueprint = Blueprint('home', __name__,template_folder='templates',static_folder='static')

navigation_bar = [
    ('/dashboard', 'dashboard', 'Home', 'home', 'material-icons'),
    ('/userInfo', 'user', 'User Profile', 'person', 'material-icons'),
    ('/table', 'table', 'Table', 'content_paste', 'material-icons'),
    ('/icons', 'icons', 'Server', '', "fa_fa-server")]


@home_blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', navigation_bar=navigation_bar,name=current_user.username)


@home_blueprint.route('/userInfo')
@login_required
def server_info():
    return render_template('user.html', navigation_bar=navigation_bar,name=current_user.username)


@home_blueprint.route('/table')
@login_required
def table_info():
    return render_template('table.html', navigation_bar=navigation_bar,name=current_user.username)

@home_blueprint.route('/icons')
def icons():
    return render_template('icons.html', navigation_bar=navigation_bar,name=current_user.username)
