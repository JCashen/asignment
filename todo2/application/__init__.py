from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import getenv

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Bungle_11@35.242.174.199/game_review'
app.config['SECRET_KEY'] = 'SECRETKEY'

from application import routes


