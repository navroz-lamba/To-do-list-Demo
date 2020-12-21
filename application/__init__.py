from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # relative path
db = SQLAlchemy(app)

from . import routes