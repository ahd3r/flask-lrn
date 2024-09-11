import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

logger = logging.getLogger('flask-app')
logger.setLevel(logging.DEBUG)
__formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
__fh = logging.FileHandler(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'flask-app.log'))
__fh.setLevel(logging.ERROR)
__fh.setFormatter(__formatter)
__ch = logging.StreamHandler()
__ch.setLevel(logging.INFO)
__ch.setFormatter(__formatter)
logger.addHandler(__fh)
logger.addHandler(__ch)

app = Flask('flask-app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'flask-app.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'migrations'))
