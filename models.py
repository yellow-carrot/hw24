from marshmallow import Schema, fields, ValidationError, validates_schema

VALID_CMD = ('filter', 'unique', 'map', 'limit', 'sort')


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema()
    def check_valid_cmd(self, value, *args, **kwargs):
        if value['cmd'] not in VALID_CMD:
            raise ValidationError('cmd not valid')


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)
