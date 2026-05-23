#server/app.py

from flask import Flask
from config import Config
from extensions import db, migrate, bcrypt, api, cors

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    api.init_app(app)
    cors.init_app(app)

    # Import models so migrate can detect them
    from models.user import User
    from models.quests import Quest

    # Register controllers
    # from controllers.quests import *

    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5555, debug=True)