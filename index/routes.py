from flask import render_template, request, redirect
from main import app, text_list
from helpers import get_user
from json_db import JsonDB


@app.route("/")
@app.route("/index")
def index():
    user = get_user(request)
    json_data = JsonDB("indices.json")
    if not user:
        return redirect("/login")
    if not (str(user.id)) in json_data.keys():
        json_data[str(user.id)] = 0
    return render_template("index.html", text=text_list[user.text_id],
                           id={'iid': user.text_id, 'strid': str(user.text_id)},
                           name=f"{user.id}_{json_data[str(user.id)] - 1}.wav")
