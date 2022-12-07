import codecs
import os
import re

import dotenv
from flask import Flask, redirect

import csv

mydict = {}
env = dotenv.dotenv_values(".env")
app = Flask(__name__)
for i in os.listdir("static/sounds"):
    os.remove("static/sounds/" + i)

with open('csv/base.csv', mode='r', newline="") as inp:
    reader = csv.reader(inp, delimiter="\t")
    text_list = [{"id": rows[0], "text": codecs.encode(rows[1], "cp1251").decode("utf-8"),
                  "instruction": codecs.encode(rows[2], "cp1251").decode("utf-8")} for rows in reader]

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

