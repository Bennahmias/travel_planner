from app import db

class Itinerary(db.Model):
    # This defines the name of the table in the database
    __tablename__ = 'itineraries'

    id = db.Column(db.Integer, primary_key=True) # Auto-incrementing primary key
    destination = db.Column(db.String(100), nullable=False) # Destination name
    days = db.Column(db.Integer, nullable=False) # Number of days in the itinerary

    # This method is used to define how the model will be represented when printed.
    def __repr__(self):
        return f"<Itinerary {self.destination}>"