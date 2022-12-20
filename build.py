import os

os.system("pip install -r requirements.txt")

paths_required = ["static/sounds", "static/ready", "logs"]

for i in paths_required:
    if not os.path.isdir(i):
        os.mkdir(i)

files_required = ["logs/texts.log", "app.db", "indices.json", "just_registered.json"]

for i in files_required:
    if not os.path.isfile(i):
        with open(i, "w"):
            pass
