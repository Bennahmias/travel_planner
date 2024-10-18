from app import db


class Place(db.Model):
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location_x = db.Column(db.Float, nullable=False)
    location_y = db.Column(db.Float, nullable=False)
    photos = db.Column(db.String(5000))
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itineraries.id'), nullable=False)

    def __repr__(self):
        return f"<Place {self.name}>"

