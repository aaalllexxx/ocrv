import os
from hashlib import sha256
from flask import render_template, request, redirect, make_response, url_for, flash
from main import app
from login.forms import LoginForm
from register.models import User
from settings import db
from uuid import uuid4
from json_db import JsonDB


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        users = db.session.query(User)
        user = users.filter_by(name=form.username.data).first() or users.filter_by(
            email=sha256(form.username.data.encode("utf-8")).hexdigest()).first()
        if user and user.password == sha256(form.password.data.encode("utf-8")).hexdigest():
            resp = make_response(redirect("/"))
            sid = uuid4().hex
            resp.set_cookie("session_id", sid, 60 * 60 * 24)
            user.session_id = sid
            db.session.commit()
            files = os.listdir("static/sounds")
            for file in files:
                if str(user.id) == file.split("_")[0]:
                    os.remove(f"static/sounds/{file}")
            json_data = JsonDB("indices.json")
            json_data[str(user.id)] = 0
            return resp
        else:
            flash("incorrect password or email")
    return render_template("login.html", form=form)
