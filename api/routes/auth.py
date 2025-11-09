from flask import Blueprint, request, jsonify
from models.user_model import UserModel
from utils.jwt_helper import generate_token, verify_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    # validation ...
    user = UserModel.create_user(data)
    return jsonify({'success': True}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    # check user, validate password, generate JWT...
    token = generate_token(data['email'])
    return jsonify({'token': token})

@auth_bp.route('/user', methods=['GET'])
def get_user():
    token = request.headers.get('Authorization').split()[1]
    user = verify_token(token)
    return jsonify({'user': user})
