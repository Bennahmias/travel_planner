from flask import Blueprint, jsonify, request
from app import db
from app.models import Itinerary



Itineraries = Blueprint('itineraries',__name__)



# add new itineraries to the database
@Itineraries.route('/itineraries', methods=['POST'])
def add_itinerary():
    data = request.get_json()

    # checks if the user accidently didnt put dest or days
    if not data or 'destination' not in data or 'days' not in data:
        return jsonify({"error": "Invalid data, no destination or days"}), 400
    
    # Create a new Itinerary object using the data provided by the client
    new_itinerary = Itinerary(
        destination=data['destination'], 
        days=data['days'], 
        user_id=data['user_id']  # Include user_id here
    )
    # This adds the new itinerary to the current database session, but it’s not yet saved.
    db.session.add(new_itinerary)
    # This commits (saves) the transaction to the database, making the changes permanent.
    db.session.commit()
    return jsonify({"message": f"Your trip to {data['destination']} added!"}), 201



# retrieve all itineraries stored in the database
@Itineraries.route('/itineraries', methods=['GET'])
def get_itineraries():
    # fetch all entries from the table. The result is a list of Itinerary objects.
    itineraries = Itinerary.query.all()  # Get all itineraries from the database
    # list of dictionaries!
    output = []
    for itinerary in itineraries:
        # creates dict with id, dest and days
        itinerary_data = {
            'id': itinerary.id,
            'destination': itinerary.destination,       
            'days': itinerary.days
        }
        output.append(itinerary_data)
    return jsonify({"itineraries list": output})