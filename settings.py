from environment import Environment
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import main

env = Environment(".env")
main.app.config.from_object(Config)
db = SQLAlchemy(main.app)
migrate = Migrate(main.app, db)
