#server/models/quests.py

from extensions import db
from sqlalchemy.orm import validates
from datetime import datetime, timezone

class Quest(db.Model):
    __tablename__ = 'quests'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default='active', nullable=False)
    difficulty = db.Column(db.String, nullable=False)
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
        return title

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
        if reward_gold < 0:
            raise ValueError('Reward gold cannot be negative.')
        return reward_gold

    def __repr__(self):
        return f'<Quest {self.title} | {self.difficulty} | {self.status}>'