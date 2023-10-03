#!/usr/bin/python3
""" starts a Flask web application that displays Hello HBNB!"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# Set strict_slashes to False
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Configures the root of the site which returns a word"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Configures the hbnb of the site which returns a word"""
    return "HBNB"


@app.route('/c/<text>')
def ctext(text):
    """ Configures c route of the site which takes a word and returns a word"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def pyth(text="is_cool"):
    """ Configures python route of the site which takes a word
    and returns a word """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:n>')
def number(n):
    """ Configures number route of the site which takes only a number
    and returns a sentence displaying given number"""
    return f"{escape(n)} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
