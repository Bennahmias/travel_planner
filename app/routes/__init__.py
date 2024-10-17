from flask import Blueprint, jsonify, request
"""A Blueprint in Flask is a way to organize your routes (or endpoints) into separate components.
Instead of having all your routes in one file, you can separate them into different modules using Blueprints. 
This helps keep your app modular, making it easier to manage as it grows."""
from app import db
from .itinerary import Itineraries
from .user import user


main = Blueprint('main',__name__)

# the main route when opening the browser
@main.route('/')
def index():
    return jsonify({"message": "Welcome to your Travel Planner!"})

# Register the Blueprints
def register_all_blueprints(app):
    app.register_blueprint(Itineraries)
    app.register_blueprint(user)