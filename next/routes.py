from main import app, text_list
from flask import redirect, request
from settings import db, env
from helpers import get_user, analise_text
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
    if env.auto_text_analise:
        index = analise_text(text_list[user.text_id]["text"])
    else:
        index = ""
    info = LogInfo(
        f"skipped text {text_list[user.text_id]['id']}{'' if not env.auto_text_analise or not index else ' with potential error in position ' + str(index[0]) + ' in word ' + index[1] + '. Word to replace: ' + index[2]} ",
        str(user.id))
    Debug.log(info, LogType.file, "logs/texts.log")
    skip(user)
    return redirect("/")


@app.route("/next")
def next_text():
    user = get_user(request)
    skip(user)
    return redirect("/")
