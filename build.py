import os

os.system(
    "pip install alembic blinker certifi charset-normalizer click colorama Flask Flask-Mail Flask-Migrate Flask-SQLAlchemy Flask-WTF greenlet idna importlib-metadata itsdangerous Jinja2 Mako MarkupSafe psycopg2 python-dotenv requests SQLAlchemy urllib3 Werkzeug WTForms zipp")
paths_required = ["static/sounds", "static/ready", "logs"]

for i in paths_required:
    if not os.path.isdir(i):
        os.mkdir(i)

files_required = ["logs/texts.log", "app.db", "indices.json", "just_registered.json"]

for i in files_required:
    if not os.path.isfile(i):
        with open(i, "w"):
            pass
