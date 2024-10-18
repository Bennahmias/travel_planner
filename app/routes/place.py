from flask import Blueprint, jsonify, request
from app import db
from app.models import Place, Itinerary

places = Blueprint('places', __name__)

# Route to add a place to an itinerary
@places.route('/itineraries/<int:itinerary_id>/places', methods=['POST'])
def add_place(itinerary_id):
    itinerary = Itinerary.query.get_or_404(itinerary_id)  # Find the itinerary by ID
    data = request.get_json()

    if not data or 'name' not in data or 'location_x' not in data or 'location_y' not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_place = Place(
        name=data['name'],
        location_x=data['location_x'],
        location_y=data['location_y'],
        photos=data.get('photos', ''),  # Optional photos field
        itinerary_id=itinerary.id
    )

    db.session.add(new_place)
    db.session.commit()

    return jsonify({"message": f"The place: {data['name']} added to itinerary {itinerary.destination}!"}), 201

# Route to get all places for a specific itinerary
@places.route('/itineraries/<int:itinerary_id>/places', methods=['GET'])
def get_places(itinerary_id):
    itinerary = Itinerary.query.get_or_404(itinerary_id)
    places = Place.query.filter_by(itinerary_id=itinerary.id).all()

    output = []
    for place in places:
        place_data = {
            'id': place.id,
            'name': place.name,
            'location_x': place.location_x,
            'location_y': place.location_y,
            'photos': place.photos
        }
        output.append(place_data)

    return jsonify({"itinerary": itinerary.destination, "places": output})
