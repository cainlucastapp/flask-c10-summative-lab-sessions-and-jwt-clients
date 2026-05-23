#server/models/quests.py

from extensions import db
from sqlalchemy.orm import validates
from datetime import datetime, timezone

class Quest(db.Model):
    __tablename__ = 'quests'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), default='active', nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    reward_gold = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


    # Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    # Validations
    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError('Title is required.')
        if not isinstance(title, str):
            raise ValueError('Title must be a string.')
        if len(title) < 2:
            raise ValueError('Title must be at least 2 characters.')
        if len(title) > 100:
            raise ValueError('Title must be 100 characters or fewer.')
        return title.strip()

    @validates('description')
    def validate_description(self, key, description):
        if not description:
            raise ValueError('Description is required.')
        if not isinstance(description, str):
            raise ValueError('Description must be a string.')
        if len(description) < 10:
            raise ValueError('Description must be at least 10 characters.')
        if len(description) > 500:
            raise ValueError('Description must be 500 characters or fewer.')
        return description.strip()

    @validates('status')
    def validate_status(self, key, status):
        valid_statuses = ['active', 'completed', 'failed']
        if status not in valid_statuses:
            raise ValueError(f'Status must be one of: {", ".join(valid_statuses)}')
        return status

    @validates('difficulty')
    def validate_difficulty(self, key, difficulty):
        valid_difficulties = ['Easy', 'Medium', 'Hard', 'Legendary']
        if difficulty not in valid_difficulties:
            raise ValueError(f'Difficulty must be one of: {", ".join(valid_difficulties)}')
        return difficulty

    @validates('reward_gold')
    def validate_reward_gold(self, key, reward_gold):
        if not isinstance(reward_gold, int):
            raise ValueError('Reward gold must be an integer.')
        if reward_gold < 0:
            raise ValueError('Reward gold cannot be negative.')
        if reward_gold > 100000:
            raise ValueError('Reward gold cannot exceed 100,000.')
        return reward_gold

    @validates('user_id')
    def validate_user_id(self, key, user_id):
        if not user_id:
            raise ValueError('user_id is required.')
        if not isinstance(user_id, int):
            raise ValueError('user_id must be an integer.')
        return user_id
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'difficulty': self.difficulty,
            'reward_gold': self.reward_gold,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def __repr__(self):
        return f'<Quest {self.title} | {self.difficulty} | {self.status}>'