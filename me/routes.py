from helpers import get_user
from flask import request, redirect
from register.models import User
from main import app


@app.route("/me")
def me():
    user = get_user(request)
    if not user:
        return redirect("/login")
    return "you: " + user.name + " id: " + str(user.id)
