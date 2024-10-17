from flask import Blueprint, jsonify, request
from app import db
from app.models import User


user = Blueprint('user',__name__)

@user.route('/user', methods = ['POST'])
def add_user():
    data = request.get_json()

    new_user = User(name = data['name'], email = data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':f'the user {data["name"]} added! and your email is: {data["email"]}'}), 201

@user.route('/user', methods = ['GET'])
def get_users_list():
    users = User.query.all()

    output = []
    for user in users:
        # creates dict with id, dest and days
        users_data = {
            'id': user.id,
            'name': user.name,       
            'email': user.email
        }
        output.append(users_data)
    return jsonify({"users list": output})