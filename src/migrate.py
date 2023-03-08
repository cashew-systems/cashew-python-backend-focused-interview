from flask_migrate import Migrate
from .flask import app
from .db import db
from .models import *

migrate = Migrate(app, db)