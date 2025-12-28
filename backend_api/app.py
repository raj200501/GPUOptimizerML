from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
if not os.getenv("DATABASE_URL"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        f"sqlite:///{os.path.abspath(os.path.join(os.path.dirname(__file__), 'gpu_optimizer.db'))}",
    )

db = SQLAlchemy(app)
CORS(app)

from routes.api_routes import app as routes_app
app.register_blueprint(routes_app)

def init_database():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    init_database()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
