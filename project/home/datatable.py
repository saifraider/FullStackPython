from project.home import home_blueprint
from flask import request
from datatables import ColumnDT, DataTables
from sqlalchemy import func
from flask import jsonify
from database import session
from project.models.user import User
from project.models.timepass import Timepass
import json


@home_blueprint.route('/datatable')
def data():

    columns = [
        ColumnDT(User.id),
        ColumnDT(User.username),
        ColumnDT(User.email)

    ]

    query = session.query(User.id, User.username, User.email)

    params = request.args.to_dict()

    rowTable = DataTables(params, query, columns)

    return jsonify(rowTable.output_result())


@home_blueprint.route('/aggregate')
def aggregate():
    columns = [
        ColumnDT(Timepass.user_name),
        ColumnDT(func.sum(Timepass.income).label('Sum'), global_search=False),
        ColumnDT(func.count(Timepass.user_name).label('Count'), global_search=False)
    ]
    query = session.query(Timepass.user_name, func.sum(Timepass.income).label('Sum'),
                          func.count(Timepass.user_name).label('Count')).group_by(Timepass.user_name)

    params = request.args.to_dict()

    rowTable = DataTables(params, query, columns)

    return jsonify(rowTable.output_result())


@home_blueprint.route('/datatable_delete')
def delete():
    user_id = request.args['id']
    user = session.query(User).filter_by(id=user_id).first()
    session.delete(user)
    session.commit()
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

    query = session.query(User.id, User.username, User.email).filter(User.id >= min_val, User.id <= max_val)

    params = request.args.to_dict()

    rowTable = DataTables(params, query, columns)

    return jsonify(rowTable.output_result())
