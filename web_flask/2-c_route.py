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
    return "C" + text.replace('_', ' ')


if __name__ == "__main__":
    app.run()
