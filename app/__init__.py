from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/asdf.db"
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)

from app import views, models
