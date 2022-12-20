import os

os.system(
    "pip install -r requirements.txt alembic==1.8.1 blinker==1.5 certifi==2022.12.7 charset-normalizer==2.1.1 click==8.1.3 colorama==0.4.6 Flask Flask-Mail Flask-Migrate Flask-SQLAlchemy Flask-WTF greenlet==2.0.1 idna==3.4 importlib-metadata==5.1.0 itsdangerous==2.1.2 Jinja2==3.1.2 Mako==1.2.4 MarkupSafe==2.1.1 psycopg2==2.9.5 python-dotenv==0.21.0 requests==2.28.1 SQLAlchemy==1.4.44 urllib3==1.26.13 Werkzeug==2.2.2 WTForms==3.0.1 zipp==3.11.0")
paths_required = ["static/sounds", "static/ready", "logs"]

for i in paths_required:
    if not os.path.isdir(i):
        os.mkdir(i)

files_required = ["logs/texts.log", "app.db", "indices.json", "just_registered.json"]

for i in files_required:
    if not os.path.isfile(i):
        with open(i, "w"):
            pass
