import json
from project.home import home_blueprint
from flask import render_template
from flask_login import login_required, current_user  # pragma: no cover
from project.models.user import User
from database import session

navigation_bar = [
    ('/dashboard', 'dashboard', 'Home', 'home', 'material-icons'),
    ('/userInfo', 'user', 'User Profile', 'person', 'material-icons'),
    ('/table', 'table', 'Table', 'content_paste', 'material-icons'),
    ('/icons', 'icons', 'Server', '', "fa_fa-server")]


@home_blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', navigation_bar=navigation_bar, current_user=current_user)


@home_blueprint.route('/userInfo')
@login_required
def server_info():
    return render_template('user.html', navigation_bar=navigation_bar, current_user=current_user)


@home_blueprint.route('/table')
@login_required
def table_info():
    return render_template('table.html', navigation_bar=navigation_bar, current_user=current_user)


@home_blueprint.route('/icons')
def icons():
    return render_template('icons.html', navigation_bar=navigation_bar, name=current_user.username)


@home_blueprint.route('/ajax')
def ajax():
    users = session.query(User).all()
    list_of_users = []
    for user in users:
        user_data = dict()
        user_data['username'] = user.username
        user_data['id'] = user.id
        user_data['email'] = user.email
        list_of_users.append(user_data)
    print(json.dumps(list_of_users))
    return json.dumps(list_of_users)
