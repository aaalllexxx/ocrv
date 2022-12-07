from hashlib import sha256

from flask import redirect
from flask import render_template, request

from main import app
from register.forms import RegisterForm
from register.models import User
from settings import db, env


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data,
                    sha256(form.email.data.encode("utf-8")).hexdigest(),
                    sha256(form.password.data.encode("utf-8")).hexdigest())
        registered_user = User.query.filter_by(
            email=sha256(form.email.data.encode("utf-8")).hexdigest()).first() or User.query.filter_by(
            name=form.username.data.encode("utf-8")).first()
        if registered_user:
            if user.email == registered_user.email and env.email_required:
                print("email already registered")
            elif user.name == registered_user.name:
                print("uname already registered")
        else:
            db.session.add(user)
            db.session.commit()
            return redirect("/login")
    return render_template("register.html", form=form, email_required=env.email_required)