from ast import literal_eval

from main import app
from flask import request, redirect, flash
from helpers import get_user
from json_db import JsonDB
import os

from settings import db


@app.route("/save", methods=["GET", "POST"])
def save():
    user = get_user(request)
    json_data = JsonDB("indices.json")
    if not user:
        return redirect("/login")
    if not (str(user.id) in json_data.keys()):
        json_data[str(user.id)] = 1
    if request.method == 'POST':
        f = request.files['voice']
        path = os.path.join('static', 'sounds', f'{user.id}_{json_data[str(user.id)] - 1}.wav')
        if os.path.exists(path):
            os.remove(path)
        f.save(f'static/sounds/{user.id}_{json_data[str(user.id)]}.wav')
        if json_data[str(user.id)] < 10:
            json_data[str(user.id)] += 1
        else:
            json_data[str(user.id)] = 0
    return redirect(f"/")


@app.route("/save_id")
def save_id():
    user = get_user(request)
    json_data = JsonDB("indices.json")
    if not user:
        return redirect("/login")
    redir = "/" + (request.args.get("redirect") or "next")
    if not (str(user.id) in json_data.keys()):
        json_data[str(user.id)] = 0
    if request.args:
        path = f"static/sounds/{user.id}_{json_data[str(user.id)]-1}.wav"
        print(os.path.exists(path))
        if os.path.exists(path):
            with open(path, "rb") as file:
                content = file.read()
            with open(f"static/ready/{user.id}_{request.args['id']}.wav", "wb") as file:
                file.write(content)
            recent = literal_eval(user.recent_texts)
            if not (user.text_id in recent) and redir == "/next":
                user.recent_texts = str(recent + [user.text_id])
                db.session.commit()
            return redirect(redir)
        else:
            flash("Мне нечего отправлять😃, запишите голос и я его отправлю")
            if not ("/save_id" in request.url):
                return redirect(request.url)
            else:
                return redirect("/index")

    return "No args"
