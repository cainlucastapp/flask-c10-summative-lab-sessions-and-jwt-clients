#server/controllers/quests.py

from flask import request, session
from flask_restful import Resource
from models.quests import Quest
from models.user import User
from extensions import db
from security.auth import login_required, current_user


class QuestList(Resource):

    @login_required
    def get(self):
        user = current_user()

        # Pagination params with safe defaults
        try:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 10))
        except ValueError:
            return {'errors': ['Page and per_page must be integers.']}, 400

        if page < 1:
            return {'errors': ['Page must be greater than 0.']}, 400
        if per_page < 1 or per_page > 50:
            return {'errors': ['per_page must be between 1 and 50.']}, 400

        # Only fetch quests belonging to current user
        paginated = Quest.query.filter_by(user_id=user.id)\
            .order_by(Quest.created_at.desc())\
            .paginate(page=page, per_page=per_page, error_out=False)

        quests = [_quest_response(q) for q in paginated.items]

        return {
            'quests': quests,
            'pagination': {
                'total': paginated.total,
                'pages': paginated.pages,
                'current_page': paginated.page,
                'per_page': paginated.per_page,
                'has_next': paginated.has_next,
                'has_prev': paginated.has_prev
            }
        }, 200

    @login_required
    def post(self):
        user = current_user()

        data = request.get_json(silent=True)
        if not data:
            return {'errors': ['Request body must be valid JSON.']}, 400

        title = data.get('title', '').strip()
        description = data.get('description', '').strip()
        difficulty = data.get('difficulty', '').strip()
        reward_gold = data.get('reward_gold', 0)

        # Validate required fields
        if not title:
            return {'errors': ['Title is required.']}, 422
        if not description:
            return {'errors': ['Description is required.']}, 422
        if not difficulty:
            return {'errors': ['Difficulty is required.']}, 422

        # reward_gold must be an integer
        if not isinstance(reward_gold, int):
            return {'errors': ['Reward gold must be an integer.']}, 422

        try:
            quest = Quest(
                title=title,
                description=description,
                difficulty=difficulty,
                reward_gold=reward_gold,
                status='active',
                user_id=user.id
            )
            db.session.add(quest)
            db.session.commit()

            return _quest_response(quest), 201

        except ValueError as e:
            db.session.rollback()
            return {'errors': [str(e)]}, 422
        except Exception as e:
            db.session.rollback()
            return {'errors': ['An unexpected error occurred.']}, 500


class QuestDetail(Resource):

    @login_required
    def patch(self, id):
        user = current_user()

        # Find quest — 404 if not found OR not theirs
        quest = Quest.query.filter_by(id=id, user_id=user.id).first()
        if not quest:
            return {'errors': ['Quest not found or unauthorized.']}, 404

        # Lock completed and failed quests
        if quest.status in ['completed', 'failed']:
            return {'errors': [f'Quest is already {quest.status} and cannot be modified.']}, 403

        data = request.get_json(silent=True)
        if not data:
            return {'errors': ['Request body must be valid JSON.']}, 400

        # Only status can be changed — ignore everything else
        new_status = data.get('status', '').strip().lower()

        if not new_status:
            return {'errors': ['Status is required.']}, 422

        valid_statuses = ['active', 'completed', 'failed']
        if new_status not in valid_statuses:
            return {'errors': [f'Status must be one of: {", ".join(valid_statuses)}']}, 422

        try:
            quest.status = new_status

            # Auto reward gold on completion
            if new_status == 'completed':
                user.gold += quest.reward_gold

            db.session.commit()

            return _quest_response(quest), 200

        except ValueError as e:
            db.session.rollback()
            return {'errors': [str(e)]}, 422
        except Exception as e:
            db.session.rollback()
            return {'errors': ['An unexpected error occurred.']}, 500

    @login_required
    def delete(self, id):
        user = current_user()

        # Find quest — 404 if not found OR not theirs
        quest = Quest.query.filter_by(id=id, user_id=user.id).first()
        if not quest:
            return {'errors': ['Quest not found or unauthorized.']}, 404

        try:
            db.session.delete(quest)
            db.session.commit()
            return {}, 204

        except Exception as e:
            db.session.rollback()
            return {'errors': ['An unexpected error occurred.']}, 500


# Private helper
def _quest_response(quest):
    return {
        'id': quest.id,
        'title': quest.title,
        'description': quest.description,
        'status': quest.status,
        'difficulty': quest.difficulty,
        'reward_gold': quest.reward_gold,
        'user_id': quest.user_id,
        'created_at': quest.created_at.isoformat(),
        'updated_at': quest.updated_at.isoformat()
    }