class BadRequestError(Exception):
  status=400
  type_error='BadRequestError'

  def __init__(self, message):
    self.message=message

class NotFoundError(Exception):
  status=404
  type_error='NotFoundError'

  def __init__(self, message):
    self.message=message

class AuthorizationError(Exception):
  status=403
  type_error='AuthorizationError'

  def __init__(self, message):
    self.message=message

class InternalError(Exception):
  status=500
  type_error='InternalError'

  def __init__(self, message):
    self.message=message
