from flask import Flask
""" SQLAlchemy is an ORM (Object-Relational Mapper) that allows you to work with databases using 
Python objects (classes) instead of writing SQL queries directly.
The Flask-SQLAlchemy extension integrates SQLAlchemy with Flask, 
simplifying the interaction between your Flask app and the database."""
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy-will handle all interactions with the database
db = SQLAlchemy()


#creating the app funcion
def create_app():
    #start the flask app
    app = Flask(__name__)

    # This line loads configuration settings from an external configuration file, typically config.py
    # app.config.from_object(): This method tells Flask to load its configuration from a Python object or class 
    # (in this case, Config inside config.py).
    app.config.from_object('config.Config')

    # Initialize the database with the app-This ties the SQLAlchemy instance to the Flask app,
    # so it knows how to interact with your Flask app and the database
    db.init_app(app)

    # Register routes
    from app.routes import main, register_all_blueprints
    # This adds all the routes defined in the main Blueprint to the app.
    app.register_blueprint(main)
    register_all_blueprints(app)

    return app
