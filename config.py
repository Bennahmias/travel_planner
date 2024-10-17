import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    # SQLite database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///travel_planner.db'  # Relative path to the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Turn off the modification tracking to save resources
    # We will add other configurations like database URI, API keys, etc.
