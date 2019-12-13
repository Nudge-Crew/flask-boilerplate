from flask import Flask, Blueprint
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import config, routes

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=config.Config.API_PREFIX)
