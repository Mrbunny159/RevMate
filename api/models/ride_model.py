from utils.db import db

class RideModel:
    @staticmethod
    def get_all_rides():
        # Return all rides from NeoDB
        pass

    @staticmethod
    def create_ride(organizer_id, data):
        # Insert ride doc
        pass

    @staticmethod
    def join_ride(ride_id, user_id):
        # Add user to ride participants
        pass
