from flask import Flask
from flask_cors import CORS

from routes.auth import auth_bp
from routes.rides import rides_bp
from routes.user import user_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(rides_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
