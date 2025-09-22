# This file is intentionally left blank.from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configurations for testing
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Home route
    @app.route('/')
    def home():
        return "Welcome to the Chat App"

    return app
