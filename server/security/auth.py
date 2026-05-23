#server/security/auth.py

from flask import request, session
from flask_restful import Resource
from models.user import User
from extensions import db


def current_user():
    #Helper to get the current logged in user from session.
    user_id = session.get('user_id')
    if not user_id:
        return None
    return db.session.get(User, user_id)


def login_required(func):
    #Decorator to protect routes that require authentication.
    def wrapper(*args, **kwargs):
        if not current_user():
            return {'errors': ['Unauthorized. Please log in.']}, 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


class Signup(Resource):
    def post(self):
        # Safely parse JSON
        data = request.get_json(silent=True)
        if not data:
            return {'errors': ['Request body must be valid JSON.']}, 400

        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '')
        password_confirmation = data.get('password_confirmation', '')
        character_class = data.get('character_class', '').strip()

        # Check required fields
        if not username:
            return {'errors': ['Username is required.']}, 422
        if not email:
            return {'errors': ['Email is required.']}, 422
        if not password:
            return {'errors': ['Password is required.']}, 422
        if not character_class:
            return {'errors': ['Character class is required.']}, 422

        # Check password length before even touching bcrypt
        if len(password) < 8:
            return {'errors': ['Password must be at least 8 characters.']}, 422

        # Check passwords match
        if password != password_confirmation:
            return {'errors': ['Passwords do not match.']}, 422

        # Check uniqueness before hitting the db
        if User.query.filter_by(username=username).first():
            return {'errors': ['Username already taken.']}, 422
        if User.query.filter_by(email=email.lower()).first():
            return {'errors': ['Email already in use.']}, 422

        try:
            user = User(
                username=username,
                email=email,
                character_class=character_class,
            )
            user.password_hash = password
            db.session.add(user)
            db.session.commit()

            session['user_id'] = user.id

            return _user_response(user), 201

        except ValueError as e:
            db.session.rollback()
            return {'errors': [str(e)]}, 422
        except Exception as e:
            db.session.rollback()
            return {'errors': ['An unexpected error occurred.']}, 500


class Login(Resource):
    def post(self):
        data = request.get_json(silent=True)
        if not data:
            return {'errors': ['Request body must be valid JSON.']}, 400

        username = data.get('username', '').strip()
        password = data.get('password', '')

        if not username:
            return {'errors': ['Username is required.']}, 422
        if not password:
            return {'errors': ['Password is required.']}, 422

        user = User.query.filter_by(username=username).first()

        if not user or not user.authenticate(password):
            return {'errors': ['Invalid username or password.']}, 401

        session['user_id'] = user.id

        return _user_response(user), 200


class CheckSession(Resource):
    def get(self):
        user = current_user()

        if not user:
            return {}, 204

        return _user_response(user), 200


class Logout(Resource):
    def delete(self):
        if not session.get('user_id'):
            return {'errors': ['No active session.']}, 401

        session.pop('user_id', None)
        return {}, 204


# Private helper — keeps responses consistent across all auth routes
def _user_response(user):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'character_class': user.character_class,
        'level': user.level,
        'gold': user.gold
    }