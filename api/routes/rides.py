from flask import Blueprint, request, jsonify
from utils.jwt_helper import verify_token
from models.ride_model import RideModel

rides_bp = Blueprint('rides', __name__)

@rides_bp.route('/rides', methods=['GET'])
def get_rides():
    rides = RideModel.get_all_rides()
    return jsonify(rides)

@rides_bp.route('/rides', methods=['POST'])
def create_ride():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    organizer_id = verify_token(token)
    data = request.json
    ride = RideModel.create_ride(organizer_id, data)
    return jsonify(ride), 201

@rides_bp.route('/rides/join/<ride_id>', methods=['POST'])
def join_ride(ride_id):
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_id = verify_token(token)
    success = RideModel.join_ride(ride_id, user_id)
    return jsonify({"success": success})

@rides_bp.route('/sos', methods=['POST'])
def send_sos():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user_id = verify_token(token)
    # Logic: Fetch user's emergency contact and send alert
    return jsonify({"message": "SOS sent!"})

