from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.models.todo import Todo
from src.routes.get import get
from src.routes.create import post
from src.routes.update import put
from src.routes.erase import erase


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    app.register_blueprint(get)
    app.register_blueprint(erase)
    app.register_blueprint(put)
    app.register_blueprint(post)
    return app