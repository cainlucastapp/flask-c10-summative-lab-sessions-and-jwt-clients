#server/config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Session cookie settings
    SESSION_COOKIE_HTTPONLY = True        # Prevents JS from accessing the cookie
    SESSION_COOKIE_SAMESITE = 'Lax'      # Allows cross-port on same machine
    SESSION_COOKIE_SECURE = False         # Must be False for local HTTP development
    
    # CORS settings
    CORS_SUPPORTS_CREDENTIALS = True      # Allows cookies to be sent cross-origin
    CORS_ORIGINS = ['http://localhost:4000']  # React client port from package.json