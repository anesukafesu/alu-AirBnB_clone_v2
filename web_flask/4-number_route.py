#!/usr/bin/python3
""" Module that creates a web server using Flask
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Index route
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """The HBNB route
    """
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """The C route
    """
    return "C " + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """The Python route
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    return str(n) + " is a number"


if __name__ == "__main__":
    app.run()
