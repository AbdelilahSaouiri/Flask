from flask import Blueprint, jsonify, request
from ..models import User
from ..extensions import db

user_bp = Blueprint('user_bp', __name__, url_prefix='/api/v1/users')

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(firstName=data['firstName'],
                     lastName=data['lastName'],
                     email=data['email'],
                     password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])
