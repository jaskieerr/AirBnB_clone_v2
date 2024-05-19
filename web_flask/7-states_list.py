#!/usr/bin/python3
'''states flask stuff'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    state = storage.all("State").values()
    return render_template("7-states_list.html", states=state)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
