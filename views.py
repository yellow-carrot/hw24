from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from models import BatchRequestSchema
from utils import build_query

main_bp = Blueprint('main', __name__)

# FILENAME = 'data/apache_logs.txt'


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json
    try:
        valid_data = BatchRequestSchema().load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400

    result = None

    for query in valid_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=valid_data['file_name'],
            data=result,
        )

    return jsonify(result)
