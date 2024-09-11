from flask import request, jsonify
import jwt

from model.User import User
from util.errors import AuthorizationError

def check_auth(controller):
  def wraped_controller(*args, **kwargs):
    token=request.headers.get('authorization')
    if token is None:
      raise AuthorizationError("Authorization token does not found in header")
    try:
      user_token_data=jwt.decode(jwt=token, algorithms=["HS256"], key="veryverysecretvalue")
    except Exception as er:
      raise AuthorizationError("Authorization token decoding failed")
    user=User.query.get(user_token_data["id"])
    if user is None:
      raise AuthorizationError("Authorization token does not match to any User")
    return controller(*args, **kwargs, user=user)
  wraped_controller.__name__ = controller.__name__
  return wraped_controller
