from flask import Flask
from .database import db
from config import Config
import click

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    from .routes import init_cli
    init_cli(app)

    return app