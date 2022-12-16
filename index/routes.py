from flask import render_template, request, redirect
from main import app, text_list
from helpers import get_user, send_mail
from json_db import JsonDB
from settings import env


@app.route("/")
@app.route("/index")
def index():
    user = get_user(request)
    json_data = JsonDB("indices.json")
    if not user:
        return redirect("/login")
    if not (str(user.id)) in json_data.keys():
        json_data[str(user.id)] = 1
    redir = request.args.get("redir") or "next"

    if request.args:
        ident = request.args.get("id")
    else:
        ident = ""
    text = text_list[int(ident) if ident and env.can_redact else user.text_id]
    identifier = ident if ident and env.can_redact else user.text_id
    name = f"{('/sounds/' + str(user.id) + '_' + str(json_data[str(user.id)] - 1))}.wav"
    return render_template("index.html", text=text, id={'iid': identifier, 'strid': str(identifier)}, name=name,
                           redirect=redir, skipbutton=not ("id" in request.args))
