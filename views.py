from typing import Tuple, Union

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from models import BatchRequestSchema
from utils import build_query

main_bp = Blueprint('main', __name__)
test_bp = Blueprint('test', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Union[Response, Tuple[Response, int]]:
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


@test_bp.route('/')
def test():
    return 'it works'
