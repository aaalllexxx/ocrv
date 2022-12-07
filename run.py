from unit import *
from main import app
from settings import env
from settings import db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=env.debug)
