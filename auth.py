# auth.py
from functools import wraps
from flask import request, jsonify
from config import SECRET_TOKEN

def token_required(f):
    """
    Decorator to enforce token-based authentication on protected endpoints.
    Expects an Authorization header with 'Bearer <token>'.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"message": "Authorization token is missing"}), 401

        token = auth_header.split(" ")[1]
        if token != SECRET_TOKEN:
            return jsonify({"message": "Invalid authorization token"}), 401
        return f(*args, **kwargs)
    return decorated
