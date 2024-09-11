from marshmallow import Schema, fields, validate

class TaskUpdate(Schema):
  state = fields.String(required=True, validate=[validate.OneOf(choices=["TODO", "IN_PROGRESS", "DONE"])])

schema_task_update = TaskUpdate()
