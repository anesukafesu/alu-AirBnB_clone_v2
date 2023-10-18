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


if __name__ == "__main__":
    app.run()
