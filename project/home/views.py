import json

from flask import render_template, Blueprint  # pragma: no cover
from flask.ext.login import login_required, current_user  # pragma: no cover
from flask import request
from datatables import ColumnDT, DataTables
from project.models.users import User
from flask import jsonify
from project import db  # pragma: no cover

# from project.models import BlogPost   # pragma: no cover

home_blueprint = Blueprint('home', __name__, template_folder='templates', static_folder='static')

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
    users = User.query.all()
    list_of_users = []
    for user in users:
        data = dict()
        data['username'] = user.username
        data['id'] = user.id
        data['email'] = user.email
        list_of_users.append(data)
    print(json.dumps(list_of_users))
    return json.dumps(list_of_users)


@home_blueprint.route('/datatable')
def data():
    """Return server side data."""
    # defining columns
    columns = [
        ColumnDT(User.id),
        ColumnDT(User.username),
        ColumnDT(User.email)

    ]

    # defining the initial query depending on your purpose
    query = User.query.with_entities(User.id, User.username, User.email)

    print(query)
    # GET parameters
    params = request.args.to_dict()

    # instantiating a DataTable for the query and table needed
    rowTable = DataTables(params, query, columns)
    print(json.dumps(rowTable.output_result()))
    # returns what is needed by DataTable
    return jsonify(rowTable.output_result())


@home_blueprint.route('/datatable_delete')
def delete():
    user_id = request.args['id']
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return json.dumps({"res": "True"})


@home_blueprint.route('/filter_id')
def filter_id():
    min_val = request.args['min']
    max_val = request.args['max']
    print min_val
    print max_val

    columns = [
        ColumnDT(User.id),
        ColumnDT(User.username),
        ColumnDT(User.email)

    ]

    # defining the initial query depending on your purpose
    # query = User.query.with_entities(User.id, User.username, User.email).filter(User.id >= min_val).filter(User.id <= max_val))
    query = db.session.query(User.id,User.username,User.email).filter(User.id >= min_val, User.id <= max_val)
    print(query)
    # GET parameters
    params = request.args.to_dict()

    # instantiating a DataTable for the query and table needed
    rowTable = DataTables(params, query, columns)
    print(json.dumps(rowTable.output_result()))
    # print(json.dumps(rowTable.output_result()))
    # returns what is needed by DataTable
    return jsonify(rowTable.output_result())
