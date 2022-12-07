import os

_basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ADMINS = frozenset(['youremail@yourdomain.com'])
    SECRET_KEY = 'This string will be replaced with a proper key in production.'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}

    THREADS_PER_PAGE = 8

    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "1234"