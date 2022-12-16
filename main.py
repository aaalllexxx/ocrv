import codecs
import os
import re
from flask import Flask
from environment import Environment
from flask_mail import Mail
import csv

mydict = {}
app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER='smtp.mail.ru',
    MAIL_PORT=25,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='a.aabdelnur@mail.ru',
    MAIL_PASSWORD='y2GQg5Dmh05jgDtPmz21',
))
mail = Mail(app)
env = Environment(".env")
for i in os.listdir("static/sounds"):
    os.remove("static/sounds/" + i)

with open('csv/base.csv', mode='r', newline="") as inp:
    reader = csv.reader(inp, delimiter="\t")
    if env.csv_headers_exist:
        reader = list(reader)[1:-1]
    text_list = [{"id": rows[0], "text": codecs.encode(rows[1], env.encoding).decode("utf-8"),
                  "instruction": codecs.encode(rows[2], env.encoding).decode("utf-8")} for rows in reader]

regexp = r"\+[^\W\d_ \n\t]"
for n, i in enumerate(text_list):
    text = list(i["text"])
    while "*" in text:
        text[text.index("*")] = "<b>"
        text[text.index("*")] = "</b>"

    while "+" in text:
        text = list("".join(text))
        try:
            plus_index = list(re.finditer(regexp, "".join(text)))[0].start()
        except IndexError:
            break
        text[plus_index] = ""
        try:
            if text[plus_index + 1] != "ё" and text[plus_index + 1] != "Ё":
                text[plus_index + 1] += u'\u0301'
        except IndexError:
            pass

    i["text"] = "".join(text)
