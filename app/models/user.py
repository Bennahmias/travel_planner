from werkzeug.security import generate_password_hash, check_password_hash
from app import db



class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password_hash = db.Column(db.String(128), nullable=False)  # Field to store hashed password
    itineraries = db.relationship('Itinerary', backref='user', lazy=True)  # One-to-many relationship with Itinerary  # One-to-many relationship with Itinerary
    """
    backref='user': This adds a reverse reference from the Itinerary model to the User model.
    In other words, if you have an Itinerary object, you can easily access the related User object through itinerary.user.
    lazy=True: This controls how the related data is loaded. When set to lazy=True, 
    SQLAlchemy will not load the related itineraries until you specifically access them. 
    This improves performance by avoiding unnecessary queries."""

    # Method to set a password (hashes the password before storing it)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Method to verify password (compares hashed version of the input with stored hash) and return bool
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<user {self.name}>"