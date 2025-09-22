from flask import Flask

def create_app():
    app = Flask(__name__)

    # Add your app configuration here
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Register blueprints or routes
    from .routes import main
    app.register_blueprint(main)

    return app