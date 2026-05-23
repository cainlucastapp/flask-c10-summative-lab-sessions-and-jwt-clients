#server/app.py

from flask import Flask
from config import Config
from extensions import db, migrate, bcrypt, api, cors
from security.auth import Signup, Login, CheckSession, Logout

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    api.init_app(app)
    cors.init_app(app, resources={r"/*": {"origins": "http://localhost:4000"}}, supports_credentials=True)

    # Import models so migrate can detect them
    from models.user import User
    from models.quests import Quest
    
    # Register auth routes
    from security.auth import Signup, Login, CheckSession, Logout
    api.add_resource(Signup, '/signup')
    api.add_resource(Login, '/login')
    api.add_resource(CheckSession, '/check_session')
    api.add_resource(Logout, '/logout')

    # Register controllers
    from controllers.quests import QuestList, QuestDetail
    api.add_resource(QuestList, '/quests')
    api.add_resource(QuestDetail, '/quests/<int:id>')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5555, debug=True)