import uuid
import enum

from db.db import db

class TaskState(enum.Enum):
  TODO = "TODO"
  IN_PROGRESS = "IN_PROGRESS"
  DONE = "DONE"

class Task(db.Model):
  __tablename__ = "task"

  id = db.Column(db.String(255), primary_key=True, nullable=False)
  name = db.Column(db.String(255), nullable=False)
  state = db.Column(db.Enum(TaskState), nullable=False)
  user_id = db.Column(db.String(255), db.ForeignKey('user.id'), nullable=False)

  def __init__(self, name, user):
    self.id = str(uuid.uuid4())
    self.name = name
    self.state = TaskState.TODO
    self.user_id = user.id

  def __str__(self):
    return f'Task <id: {self.id}, name: {self.name}, state: {self.state}>'

  def __repr__(self):
    return f'Task <id: {self.id}, name: {self.name}, state: {self.state}>'
