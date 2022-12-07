from main import app, text_list
from flask import redirect, request
from settings import db
from helpers import get_user
from logger import Debug, LogInfo, LogType


def skip(user):
    if not user:
        return redirect("/login")
    if user.text_id < len(text_list) - 1:
        user.text_id += 1
    else:
        user.text_id = 0
    db.session.commit()


@app.route("/skip")
def skip_text():
    user = get_user(request)
    skip(user)
    info = LogInfo(f"skipped text {text_list[user.text_id]['id']}", str(user.id))
    Debug.log(info, LogType.file, "logs/texts.log")
    return redirect("/")


@app.route("/next")
def next_text():
    user = get_user(request)
    skip(user)
    return redirect("/")
