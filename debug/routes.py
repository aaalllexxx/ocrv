from settings import env, db
from main import app
from register.models import User


@app.route("/clear")
def clear():
    if env.debug:
        User.query.delete()
        db.session.commit()
        return "cleared"
