#!/usr/bin/python3
""" printing lists of state"""

from flask import Flask, render_template
from models import *
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    '''
    Lists all states from db storage
    '''
    state_dict = storage.all(State)
    state_list = list(state_dict.values())
    return render_template('7-states_list.html', state_list=state_list)


@app.teardown_appcontext
def teardown_app(e):
    '''
    closing app
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
