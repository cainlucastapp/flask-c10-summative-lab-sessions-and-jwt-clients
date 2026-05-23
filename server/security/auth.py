from functools import wraps
from flask import session
from models.user import User
from extensions import db


def current_user():
    """Helper to get the current logged in user from session."""
    user_id = session.get('user_id')
    if not user_id:
        return None
    return db.session.get(User, user_id)


def login_required(func):
    """Decorator to protect routes that require authentication."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user():
            return {'errors': ['Unauthorized. Please log in.']}, 401
        return func(*args, **kwargs)
    return wrapper