from flask_sqlalchemy import SQLAlchemy
from .flask import app

db = SQLAlchemy(app)