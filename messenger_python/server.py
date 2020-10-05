import time
from flask import Flask, Response, request
from datetime import datetime


app = Flask(__name__)
db = [
    {"text": "Hello", "author": "Jack", "time": time.time()},
    {"text": "Hello", "author": "Mary", "time": time.time()}
]


@app.route("/")
def hello():
    return "Hello, world!<br><a href='/status'>Status</a>"


@app.route("/status")
def status():
    dn = datetime.now()
    return {
        "status": True,
        "name": "LeoMessenger",
        "time": dn.isoformat(),
        }


@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    if not isinstance(data, dict):
        return Response("not json", 400)

    text = data.get("text")
    author = data.get("author")

    if isinstance(text, str) and isinstance(author, str):
        db.append({
            "text": text,
            "author": author,
            "time": time.time()
        })
        return Response("ok")
    else:
        return Response("wrong format", 400)


@app.route("/get_messages")
def get_messages():
    after = request.args.get("after", "0")

    try:
        after = float(after)
    except ValueError:
        return Response("wrong format", 400)

    new_messages = [message for message in db if message["time"] > after]
    return {"messages": new_messages}


app.run()
