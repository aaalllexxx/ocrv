from environment import Environment
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import main

env = Environment(".env")
main.app.config.from_object(Config)
db = SQLAlchemy(main.app)
migrate = Migrate(main.app, db)
base_dir = os.path.join(*(__file__.split(os.sep)[:-1]))

