from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MongoEngine(app)

from . import views
from . import models
