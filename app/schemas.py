from marshmallow import Schema, fields, validate, ValidationError


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=80))
    default_currency_id = fields.Int(required=True)


class DepositSchema(Schema):
    amount = fields.Float(required=True)
    currency_id = fields.Int(required=True)


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    amount = fields.Float(required=True, validate=validate.Range(min=0.01))
    currency_id = fields.Int(required=False)
