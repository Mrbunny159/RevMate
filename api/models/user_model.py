from utils.db import db

class UserModel:
    @staticmethod
    def create_user(data):
        # Hash password, insert user doc to NeoDB users collection
        pass

    @staticmethod
    def get_user(user_id):
        # Return user by ID
        pass

    @staticmethod
    def verify_credentials(email, password):
        # Fetch user, check hash
        pass

    @staticmethod
    def update_user(user_id, data):
        # Update fields
        pass

    @staticmethod
    def delete_user(user_id):
        # Remove user doc
        pass

    @staticmethod
    def is_email_available(email):
        # Query users
        pass

