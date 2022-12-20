import smtplib
from uuid import uuid4
from hashlib import sha256

from flask import redirect, flash
from flask import render_template, request

from helpers import send_mail
from json_db import JsonDB
from logger import Debug, LogType, LogInfo
from main import app
from register.forms import RegisterForm
from register.models import User
from settings import db, env

session_data = {}


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    json_data = JsonDB("just_registered.json")
    if request.method == 'POST' and form.validate():
        user = User(form.username.data,
                    form.email.data if form.email else "",
                    sha256(form.password.data.encode("utf-8")).hexdigest())
        registered_user = User.query.filter_by(
            email=form.email.data if form.email else "").first() or User.query.filter_by(
            name=form.username.data).first()
        if registered_user:
            if user.email == registered_user.email and env.email_required:
                flash("Почта уже зарегистрирована")
            elif user.name == registered_user.name:
                flash("Имя пользователя уже существует")
        else:
            if not env.email_required:
                db.session.add(user)
                db.session.commit()
                return redirect("/login")
            else:
                ident = uuid4()
                session_data[ident.hex] = user
                mail = str(sha256(user.email.encode("utf-8")).hexdigest())
                link = request.base_url + "?id=" + ident.hex + "&email=" + mail
                json_data[ident.hex] = mail
                try:
                    send_mail("OCRV registration", "Ваша ссылка для подтверждения регистрации: " + link, user.email)
                    flash("Сообщение отправлено")
                except:
                    flash("Не удалось отправить сообщение")
    if json_data and ("id" in request.args) and ("email" in request.args) and json_data[request.args["id"]] == \
            request.args["email"]:
        Debug.log(LogInfo("Регистрация", request.args["id"]), LogType.console)
        json_data.delete_item(request.args["id"])
        db.session.add(session_data[request.args["id"]])
        db.session.commit()
        return redirect("/login")
    return render_template("register.html", form=form, email_required=env.email_required)
