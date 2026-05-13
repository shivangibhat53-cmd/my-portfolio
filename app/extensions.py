from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_view = "auth.login"

def init_extensions(app: Flask):
    db.init_app(app)  # DB, login manager, etc will go here later
    login_manager.init_app(app)