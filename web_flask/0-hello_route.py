#!/usr/bin/python3
""" starts a Flask web application that displays Hello HBNB!"""

from flask import Flask

app = Flask(__name__)

# Set strict_slashes to False
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
