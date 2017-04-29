from datatables import ColumnDT, DataTables
from project.home import home_blueprint
from project.models.users import User
from flask import jsonify
from project import db
from flask import request
import json


@home_blueprint.route('/datatable')
def data():
    columns = [
        ColumnDT(User.id),
        ColumnDT(User.username),
        ColumnDT(User.email)

    ]
    query = User.query.with_entities(User.id, User.username, User.email)
    params = request.args.to_dict()
    rowTable = DataTables(params, query, columns)
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

    query = db.session.query(User.id,User.username,User.email).filter(User.id >= min_val, User.id <= max_val)
    params = request.args.to_dict()
    rowTable = DataTables(params, query, columns)
    # print(json.dumps(rowTable.output_result()))
    return jsonify(rowTable.output_result())
