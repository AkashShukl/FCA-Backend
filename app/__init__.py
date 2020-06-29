from flask import Flask
from flask_cors import CORS

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import routes, models
