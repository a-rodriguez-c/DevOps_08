import os
from functools import wraps
from flask import request, jsonify

# Decorator for Bearer token authentication
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # inyecto un error de variable no definida:
        print(error['error'])
        token = None

        # Check if 'Authorization' header is present
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            # Extract the token after "Bearer"
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]

        SECRET_TOKEN = os.getenv("SECRET_TOKEN")
        # Check if token matches the static token
        if not token or token != SECRET_TOKEN:
            return jsonify({'message': 'Token is missing or invalid!'}), 401

        return f(*args, **kwargs)

    return decorated
