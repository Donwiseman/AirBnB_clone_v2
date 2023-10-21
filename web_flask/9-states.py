#!/usr/bin/python3
""" starts a Flask web application. """

from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage, State

app = Flask(__name__)

# Set strict_slashes to False
app.url_map.strict_slashes = False


@app.teardown_appcontext
def app_teardown(exception=None):
    """ Ends SQLAlchey session after each request session. """
    storage.close()


@app.route('/states', defaults={'id': ''})
@app.route('/states/<id>')
def states(id=''):
    """Returns HTML that displays a list of all available states
    and their cities if specified. """
    states = storage.all(State)
    return render_template('9-states.html', n=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)