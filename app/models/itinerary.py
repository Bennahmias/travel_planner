from app import db

# This defines a model in SQLAlchemy. A model in this context is a Python class that represents a table in the database.
# By inheriting from "db.Model", you are telling SQLAlchemy that this class should be mapped to a database table.
class Itinerary(db.Model):

    # This is a special SQLAlchemy variable that defines the name of the table. In this case, the table will be named itineraries
    __tablename__ = 'itineraries'

    # db.Column: This defines a column in the table.
    # By default, if you set primary_key=True on an integer column, it will auto-increment, 
    id = db.Column(db.Integer, primary_key=True) # Auto-incrementing primary key
    # nullable = False - If a user tries to create an itinerary without a destination, the database will raise an error
    destination = db.Column(db.String(50), nullable=False) # Destination name
    days = db.Column(db.Integer, nullable=False) # Number of days in the itinerary
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to link to User
    places = db.relationship('Place', backref='itinerary', lazy=True)  # One-to-many relationship with Place


    # This is a special method in Python called __repr__. It is used to provide a string representation of the object
    # (in this case, an instance of the Itinerary class).
    # Purpose: When you print an object or inspect it in the Python shell, __repr__ defines how that object is represented.
    def __repr__(self):
        return f"<Itinerary {self.destination}>"
    

    