from flask import Blueprint, jsonify, request
"""A Blueprint in Flask is a way to organize your routes (or endpoints) into separate components.
Instead of having all your routes in one file, you can separate them into different modules using Blueprints. 
This helps keep your app modular, making it easier to manage as it grows."""

from app import db
from app.models.models import Itinerary


main = Blueprint('main',__name__)


# the main route when opening the browser
@main.route('/')
def index():
    return jsonify({"message": "Welcome to your Travel Planner!"})

# add new itineraries to the database
@main.route('/itineraries', methods=['POST'])
def add_itinerary():
    data = request.get_json()

    if not data or 'destination' not in data or 'days' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    # This creates a new Itinerary object using the data provided by the client.
    new_itinerary = Itinerary(destination=data['destination'], days=data['days'])
    # This adds the new itinerary to the current database session, but it’s not yet saved.
    db.session.add(new_itinerary)
    # This commits (saves) the transaction to the database, making the changes permanent.
    db.session.commit()
    return jsonify({"message": f"Your trip to {data['destination']} added!"}), 201



# retrieve all itineraries stored in the database
@main.route('/itineraries', methods=['GET'])
def get_itineraries():
    # This queries the database to retrieve all itineraries
    itineraries = Itinerary.query.all()  # Get all itineraries from the database
    # list of trips
    output = []
    for itinerary in itineraries:
        itinerary_data = {
            'id': itinerary.id,
            'destination': itinerary.destination,
            'days': itinerary.days
        }
        output.append(itinerary_data)
    return jsonify({"itineraries": output})