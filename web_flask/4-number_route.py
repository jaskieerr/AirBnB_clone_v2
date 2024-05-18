#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text=None):
    if text is not None:
        return "Python {}".format(text.replace("_", " "))
    return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def outint(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
