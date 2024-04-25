from flask import Blueprint, request, jsonify

from src.db.functions import db_add_record, db_get_record, db_get_aggregation_data

api_bp = Blueprint(name='api', import_name=__name__, url_prefix='/api/')


@api_bp.get('/get-data')
def get_data():
    sort = request.args.get('sort', 'default')
    records = db_get_record(sort=sort)
    return jsonify(records), 200


@api_bp.get('/get-aggregation-data')
def get_aggregation_data():
    data = db_get_aggregation_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({'message': 'bad request'}), 400


@api_bp.post('/save-data')
def save_data():
    cpu_percent = request.json.get('cpu_percent')
    db_add_record(cpu_percent)
    return jsonify({'message': 'Data saved successfully'}), 200
