from marshmallow import Schema, fields, validate

class UserAuth(Schema):
  name = fields.String(required=True, validate=[validate.Length(min=5, max=255), validate.Regexp(r"[a-zA-Z]")])
  password = fields.String(required=True, validate=[validate.Length(min=8, max=16), validate.Regexp(r"[a-z]")])

schema_user_auth = UserAuth()
