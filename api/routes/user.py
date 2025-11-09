
from flask import Blueprint, request, jsonify
from utils.jwt_helper import verify_token
from models.user_model import UserModel

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['GET'])
def get_user():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_id = verify_token(token)
    user = UserModel.get_user(user_id)
    return jsonify(user)

@user_bp.route('/user/update', methods=['PUT'])
def update_user():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_id = verify_token(token)
    data = request.json
    updated = UserModel.update_user(user_id, data)
    return jsonify({"success": updated})

@user_bp.route('/user/delete', methods=['DELETE'])
def delete_user():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_id = verify_token(token)
    UserModel.delete_user(user_id)
    return jsonify({"success": True})
