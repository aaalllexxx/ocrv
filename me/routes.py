from ast import literal_eval
from main import text_list

from helpers import get_user
from flask import request, redirect, render_template
from main import app
from settings import env


@app.route("/me")
def me():
    user = get_user(request)
    if not user:
        return redirect("/login")
    user.recent_texts = literal_eval(str(user.recent_texts))
    return render_template("me.html", user=user, texts=text_list, can_redact=env.can_redact)
