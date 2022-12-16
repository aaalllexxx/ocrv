import os
from environment import Environment

_basedir = os.path.abspath(os.path.dirname(__file__))
env = Environment(".env")


class Config(object):
    SECRET_KEY = 'This string will be replaced with a proper key in production.'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}

    THREADS_PER_PAGE = 8

    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "1234"
    MAIL_SERVER = "smtp.mail.ru"
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'a.aabdelnur@mail.com'
    MAIL_DEFAULT_SENDER = env.mail_user
    MAIL_PASSWORD = env.mail_token
