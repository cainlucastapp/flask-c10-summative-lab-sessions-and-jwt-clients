#server/models/user.py

from extensions import db, bcrypt
from sqlalchemy.orm import validates
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    character_class = db.Column(db.String, nullable=False)
    level = db.Column(db.Integer, default=1, nullable=False)
    gold = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


    # Relationship
    quests = db.relationship('Quest', backref='user', lazy=True, cascade='all, delete-orphan')


    # Password hashing
    @property
    def password_hash(self):
        raise AttributeError('Password hashes is forbidden.')

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)


    # Validations
    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError('Username is required.')
        if User.query.filter_by(username=username).first():
            raise ValueError('Username already taken.')
        return username
    
    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise ValueError('Email is required.')
        if '@' not in email:
            raise ValueError('Invalid email address.')
        if User.query.filter_by(email=email).first():
            raise ValueError('Email already in use.')
        return email

    @validates('character_class')
    def validate_character_class(self, key, character_class):
        valid_classes = ['Fighter', 'Mage', 'Rogue', 'Paladin', 'Ranger']
        if character_class not in valid_classes:
            raise ValueError(f'Character class must be one of: {", ".join(valid_classes)}')
        return character_class

    def __repr__(self):
        return f'<User {self.username} | {self.character_class} | Level {self.level}>'