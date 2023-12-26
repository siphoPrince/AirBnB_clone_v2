#!/usr/bin/python3
"""displaying in format"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Returns 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Replaces underscore symbols with a space and returns 'C {}'."""
    text = escape(text).replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python_text(text='is cool'):
    """Replaces underscore symbols with a space and returns 'Python {}'."""
    text = escape(text).replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Returns '{} is a number'."""
    return '{} is a number'.format(n)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ return in format"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
