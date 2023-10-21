#!/usr/bin/python3
""" starts a Flask web application. """

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown(exception=None):
    """ Ends SQLAlchey session after each request session. """
    storage.close()


@app.route('/states', defaults={'id': ''}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=''):
    """Returns HTML that displays a list of all available states
    and their cities if specified. """
    states = storage.all(State)
    return render_template('9-states.html', n=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
