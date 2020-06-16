from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from db_config import db_config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_config['mysql']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["MONGO_URI"] = db_config['mongo']
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = SQLAlchemy(app)
mongo = PyMongo(app)