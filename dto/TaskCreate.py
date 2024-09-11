from marshmallow import Schema, fields, validate

class TaskCreate(Schema):
  name = fields.String(required=True, validate=[validate.Length(min=1, max=255)])

schema_task_create = TaskCreate()
