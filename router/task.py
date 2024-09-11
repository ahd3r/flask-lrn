from flask import jsonify, request

from db.db import app, db
from model.Task import Task, TaskState
from dto.TaskCreate import schema_task_create
from dto.TaskUpdate import schema_task_update
from util.guard import check_auth
from util.errors import BadRequestError, NotFoundError

@app.route('/task', methods=["GET"])
@check_auth
def get_tasks(user):
  tasks = Task.query.filter_by(user_id=user.id).all()
  return jsonify({
    "data": list(map(lambda task: str(task), tasks))
  })

@app.route('/task', methods=["POST"])
@check_auth
def create_task(user):
  task_data = request.json
  errors = schema_task_create.validate(task_data)
  if bool(errors):
    raise BadRequestError(errors)
  created_task = Task(task_data["name"], user)
  db.session.add(created_task)
  db.session.commit()
  return jsonify({
    "data": str(created_task)
  }), 201

@app.route('/task/<task_id>', methods=["PATCH"])
@check_auth
def update_task_state(user, task_id):
  update_task_data = request.json
  errors = schema_task_update.validate(update_task_data)
  if bool(errors):
    raise BadRequestError(errors)
  task_to_update = Task.query.get(task_id)
  if task_to_update is None or task_to_update.user_id != user.id:
    raise NotFoundError(f"Task with if {task_id} does not exist")
  task_to_update.state = TaskState[update_task_data["state"]]
  db.session.commit()
  return jsonify({
    "data": str(task_to_update)
  }), 200

@app.route('/task/<task_id>', methods=["DELETE"])
@check_auth
def delete_task(user, task_id):
  task_query_to_delete = Task.query.filter_by(id=task_id)
  deleted_task=task_query_to_delete.first()
  if deleted_task in None or deleted_task.user_id != user.id:
    raise NotFoundError(f"Task with if {task_id} does not exist")
  task_query_to_delete.delete()
  return jsonify({
    "data": str(deleted_task)
  }), 200
