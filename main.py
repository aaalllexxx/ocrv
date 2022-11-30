from flask import Flask, render_template, request, redirect
import dotenv
import csv
import codecs
import os

mydict = {}
env = dotenv.dotenv_values(".env")
app = Flask(__name__)
debug = env["DEBUG"]
texts = {"132702": 0}
for i in os.listdir("static/sounds"):
    os.remove("static/sounds/" + i)

with open('csv/base.csv', mode='r', newline="") as inp:
    reader = csv.reader(inp, delimiter="\t")
    print(reader.__next__())
    text_list = [{"id": rows[0], "text": codecs.encode(rows[1], "cp1251").decode("utf-8"),
                  "instruction": codecs.encode(rows[2], "cp1251").decode("utf-8")} for rows in reader]
user_id = "132702"
i = 0


@app.route("/")
@app.route("/index")
def index():
    ident = request.args.get("id")
    ident = int(ident) if ident else 0
    return render_template("index.html", text=text_list[texts[user_id]], id={'iid': ident, 'strid': str(ident)},
                           name=(os.listdir("static/sounds") or [""])[0])


@app.route("/save", methods=["GET", "POST"])
def save():
    global i
    if request.method == 'POST':
        f = request.files['voice']
        path = os.path.join('static', 'sounds', f'{f.filename}{i}.wav')
        if os.path.exists(path):
            os.remove(path)
        if i < 10:
            i += 1
        else:
            i = 0
        f.save(f'static/sounds/{f.filename}{i}.wav')
    return redirect(f"/")


@app.route("/next")
def next_text():
    global i
    if texts[user_id] < len(text_list) - 1:
        texts[user_id] += 1
    else:
        texts[user_id] = 0
    return redirect(f"/")


@app.route("/save_id")
def save_id():
    if request.args:
        with open(f"static/sounds/{os.listdir('static/sounds')[0]}", "rb") as file:
            content = file.read()
        with open(f"static/ready/{request.args['id']}.wav", "wb") as file:
            file.write(content)
        return redirect("/next")
    return "No args"


if __name__ == "__main__":
    app.run(debug=debug)
