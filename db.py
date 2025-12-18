from flask import Flask
from models import db  # dein db = SQLAlchemy() aus models.py

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"   # Datei app.db im Projektordner
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # <-- erstellt alle Tabellen aus deinen db.Model Klassen
