from marshmallow import Schema, fields, validate

class UserUpdate(Schema):
  old_password = fields.String(required=True, validate=[validate.Length(min=8, max=16), validate.Regexp(r"[a-z]")])
  new_password = fields.String(required=True, validate=[validate.Length(min=8, max=16), validate.Regexp(r"[a-z]")])

schema_user_update = UserUpdate()
