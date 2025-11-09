import jwt
import datetime

JWT_SECRET = "your-secret"
JWT_ALGO = "HS256"

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)

def verify_token(token):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        return decoded["user_id"]
    except Exception:
        return None

