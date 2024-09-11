from marshmallow import Schema, fields, validate

class UserCreate(Schema):
  name = fields.String(required=True, validate=[validate.Length(min=5, max=255), validate.Regexp(regex='^[a-z]*$', flags=0, error='Should be alphabetic and lowercase')])
  password = fields.String(required=True, validate=[validate.Length(min=8, max=16), validate.Regexp(regex='^[a-z]*$', flags=0, error='Should be alphabetic and lowercase')])

schema_user_create = UserCreate()
