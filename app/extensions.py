from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_extensions(app: Flask):
    db.init_app(app)  # DB, login manager, etc will go here later