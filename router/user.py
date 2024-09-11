from flask import jsonify, request
import jwt
import bcrypt

from db.db import app, db
from model.User import User
from dto.UserCreate import schema_user_create
from dto.UserUpdate import schema_user_update
from dto.UserAuth import schema_user_auth
from util.errors import BadRequestError, NotFoundError

@app.route('/user/<user_id>', methods=["GET"])
def read_users(user_id):
  user = User.query.get(user_id)
  if user is None:
    raise NotFoundError(f"User with id {user_id} does not exist")
  return jsonify({
    "data": str(user)
  }), 200

@app.route('/user', methods=["POST"])
def create_user():
  user_data = request.json
  errors = schema_user_create.validate(user_data)
  if bool(errors):
    raise BadRequestError(errors)
  user_with_same_name = User.query.filter_by(name=user_data["name"]).first()
  if user_with_same_name is not None:
    raise BadRequestError("Name already exist")
  created_user = User(user_data["name"], bcrypt.hashpw(user_data["password"].encode(), bcrypt.gensalt(6)).decode())
  db.session.add(created_user)
  db.session.commit()
  return jsonify({
    "data": str(created_user)
  }), 201

@app.route('/user/auth', methods=["POST"])
def auth_users():
  auth_data = request.json
  errors = schema_user_auth.validate(auth_data)
  if bool(errors):
    raise BadRequestError(errors)
  user_to_auth = User.query.filter_by(name=auth_data["name"]).first()
  if user_to_auth is None:
    raise BadRequestError("Name does not exist")
  if not bcrypt.checkpw(auth_data["password"].encode(), user_to_auth.password.encode()):
    raise BadRequestError("Passwords does not match")
  return jsonify({
    "data": jwt.encode({"id": user_to_auth.id}, "veryverysecretvalue")
  }), 200

@app.route('/user/<user_id>', methods=["PATCH"])
def update_user(user_id):
  user_update_data = request.json
  errors = schema_user_update.validate(user_update_data)
  if bool(errors):
    raise BadRequestError(errors)
  user_to_update = User.query.get(user_id)
  if user_to_update is None:
    raise NotFoundError(f"User with id {user_id} does not exist")
  if not bcrypt.checkpw(user_update_data["old_password"].encode(), user_to_update.password.encode()):
    raise BadRequestError("Passwords does not match")
  user_to_update.password = bcrypt.hashpw(user_update_data["password"].encode(), bcrypt.gensalt(6)).decode()
  db.session.commit()
  return jsonify({
    "data": str(user_to_update)
  }), 200
