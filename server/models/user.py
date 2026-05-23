#server/models/user.py

from extensions import db, bcrypt
from sqlalchemy.orm import validates
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password_hash = db.Column(db.String(128), nullable=False)
    character_class = db.Column(db.String(20), nullable=False)
    level = db.Column(db.Integer, default=1, nullable=False)
    gold = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


    # Relationship
    quests = db.relationship('Quest', backref='user', lazy=True, cascade='all, delete-orphan')


    # Password protection
    @property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        if not isinstance(password, str) or len(password) < 8:
            raise ValueError('Password must be at least 8 characters.')
        self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)


    # Validations
    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError('Username is required.')
        if not isinstance(username, str):
            raise ValueError('Username must be a string.')
        if len(username) < 2:
            raise ValueError('Username must be at least 2 characters.')
        if len(username) > 50:
            raise ValueError('Username must be 50 characters or fewer.')
        return username

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise ValueError('Email is required.')
        if not isinstance(email, str):
            raise ValueError('Email must be a string.')
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email address.')
        if len(email) > 120:
            raise ValueError('Email must be 120 characters or fewer.')
        return email.lower().strip()

    @validates('character_class')
    def validate_character_class(self, key, character_class):
        valid_classes = ['Fighter', 'Mage', 'Rogue', 'Paladin', 'Ranger']
        if character_class not in valid_classes:
            raise ValueError(f'Character class must be one of: {", ".join(valid_classes)}')
        return character_class

    @validates('level')
    def validate_level(self, key, level):
        if not isinstance(level, int):
            raise ValueError('Level must be an integer.')
        if level < 1:
            raise ValueError('Level cannot be less than 1.')
        if level > 100:
            raise ValueError('Level cannot exceed 100.')
        return level

    @validates('gold')
    def validate_gold(self, key, gold):
        if not isinstance(gold, int):
            raise ValueError('Gold must be an integer.')
        if gold < 0:
            raise ValueError('Gold cannot be negative.')
        return gold

    def __repr__(self):
        return f'<User {self.username} | {self.character_class} | Level {self.level}>'