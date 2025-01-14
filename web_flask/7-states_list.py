#!/usr/bin/python3
""" starts a Flask web application that displays Hello HBNB!"""

from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage, State

app = Flask(__name__)

# Set strict_slashes to False
app.url_map.strict_slashes = False


@app.route('/states_list')
def state_list():
    """ Displays a list of all available states """
    states = storage.all(State)
    return render_template('7-states_list.html', n=states)


@app.teardown_appcontext
def app_teardown(exception=None):
    """ Help in closing each request session. """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
