#!/usr/bin/python3
"""
Starts a Flask web application to display states and cities in alphabetical order.
"""

from flask import Flask, render_template
from models import *
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a web page with a list of states and their cities in alphabetical order."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage connection on application teardown."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
