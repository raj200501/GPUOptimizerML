from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from routes.api_routes import app as routes_app
app.register_blueprint(routes_app)
