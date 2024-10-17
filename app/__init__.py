from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy-will handle all interactions with the database
db = SQLAlchemy()


#creating the app funcion
def create_app():
    #start the flask app
    app = Flask(__name__)

    # Load configuration settings from config.py
    app.config.from_object('config.Config')

    # Initialize the database with the app-This ties the SQLAlchemy instance to the Flask app,
    # so it knows how to interact with your Flask app and the database
    db.init_app(app)

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app
