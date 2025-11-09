from flask import Blueprint, request, jsonify
from models.user_model import UserModel
from utils.jwt_helper import generate_token, verify_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if not UserModel.is_email_available(data["email"]):
        return jsonify({"error": "Email already registered"}), 400
    user = UserModel.create_user(data)
    token = generate_token(user["user_id"])
    return jsonify({"token": token}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = UserModel.verify_credentials(data["email"], data["password"])
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    token = generate_token(user["user_id"])
    return jsonify({"token": token})

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # Stateless logout: frontend simply discards the JWT token
    return jsonify({"message": "Logged out"})
