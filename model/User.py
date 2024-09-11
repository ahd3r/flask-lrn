import uuid
from datetime import datetime

from db.db import db

class User(db.Model):
  __tablename__ = "user"

  id = db.Column(db.String(255), primary_key=True, nullable=False)
  name = db.Column(db.String(255), nullable=False, unique=True)
  password = db.Column(db.String(255), nullable=False)
  registered = db.Column(db.DateTime, nullable=False)

  def __init__(self, name, password):
    self.id = str(uuid.uuid4())
    self.name = name
    self.password = password
    self.registered = datetime.utcnow()

  def __str__(self):
    return f'User <id: {self.id}, name: {self.name}, password: {self.password}, registered: {self.registered}>'

  def __repr__(self):
    return f'User <id: {self.id}, name: {self.name}, password: {self.password}, registered: {self.registered}>'
