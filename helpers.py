from register.models import User
from flask_mail import Message
from main import mail
from settings import env
import requests


def check_login(request):
    ident = request.cookies.get("session_id")
    sid = User.query.filter_by(session_id=ident).first()
    if sid is None:
        return False
    return True


def get_user(request):
    return User.query.filter_by(session_id=request.cookies.get("session_id")).first() or False


def send_mail(subject, message, mail_to):
    msg = Message(subject, sender=env.mail_user, recipients=[mail_to])
    msg.body = message
    mail.send(msg)


def analise_text(text):
    url = f"https://speller.yandex.net/services/spellservice.json/checkText?text={text.replace(' ', '+')}"
    resp = requests.get(url)
    if resp.status_code == 200:
        try:
            return [text.index(resp.json()[0]["word"]), resp.json()[0]["word"], resp.json()[0]["s"][0]]
        except IndexError:
            pass
    return False
