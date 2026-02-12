from flask import Flask, request, jsonify, url_for, Blueprint
from models import User, Location, Character, db


api = Blueprint('api', __name__)

@api.route('/user', methods=['GET'])

def user():

    users = User.query.all()

    response = [user.serialize() for user in users ]

    return jsonify(response), 200




@api.route('/user/<int:id>', methods=['GET'])

def get_user(id):

    user = User.query.get(id)

    if not user : 
        return jsonify({"error": "not found"}), 404
    
    return jsonify(user.serialize()), 200


@api.route('/location', methods=['GET'])

def location():

    locations = Location.query.all()

    response = [location.serialize() for location in locations]

    return jsonify(response), 200


@api.route('/location/<int:id>', methods=['GET'])

def get_location(id):

    location = Location.query.get(id)

    if not location : 
        return jsonify({"error": "dont exist"}), 404
    
    return jsonify(location.serialize()), 200


@api.route('/character', methods=['GET'])

def character():

    characters = Character.query.all()

    response = [character.serialize() for character in characters ]

    return jsonify(response), 200

@api.route('/character/<int:id>', methods=['GET'])

def get_character(id):

    character = Character.query.get(id)

    if not character : 
        return jsonify({"error": "not found"}), 404
    
    return jsonify(character.serialize()), 200

@api.route('/user/<int:id>/location/<int:location_id>', methods=['POST'])

def add_favorites_location(id, location_id):

    user = User.query.get(id)

    location = Location.query.get(location_id)

    if not user or not location: 
        return jsonify({"error": "not found"}), 404

    user.favorite_location_list.append(location)

    db.session.commit()

    return jsonify(user.serialize_with_favorites()), 200


@api.route('/user/<int:id>/character/<int:character_id>', methods=['POST'])

def add_favorites_character(id, character_id):

    user = User.query.get(id)

    character = Character.query.get(character_id)

    if not user or not character:
        return jsonify({"error": "not found"}), 404

    user.favorite_character_list.append(character)

    db.session.commit()
     
    return jsonify(user.serialize_with_favorites()), 200

@api.route('/user/<int:id>/location/<int:location_id>', methods=['DELETE'])

def delete_favorites_location(id, location_id):

    user = User.query.get(id)
    
    location = Location.query.get(location_id)

    if not user or not location:
        return jsonify({"error": "not found"}), 404

    if location not in user.favorite_location_list:
        return jsonify({"error": "location not in favorites"}), 400

    user.favorite_location_list.remove(location)
    db.session.commit()

    return jsonify(user.serialize_with_favorites()), 200


@api.route('/user/<int:id>/character/<int:character_id>', methods=['DELETE'])

def delete_favorites_character(id, character_id):

    user = User.query.get(id)
    character = Character.query.get(character_id)

    if not user or not character:
        return jsonify({"error": "not found"}), 404

    if character not in user.favorite_character_list:
        return jsonify({"error": "character not in favorites"}), 400

    user.favorite_character_list.remove(character)
    db.session.commit()

    return jsonify(user.serialize_with_favorites()), 200


