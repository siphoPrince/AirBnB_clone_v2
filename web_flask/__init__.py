#!/usr/bin/env python3
# __init__.py

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Import the routes module to ensure the routes are registered with the app
from . import routes

