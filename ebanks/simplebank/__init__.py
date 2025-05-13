from flask import Flask
from .routes import api_bp
from .errors import register_error_handlers
from .config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)                # Load application configuration (DEBUG, TESTING, etc.)
    app.register_blueprint(api_bp)                      # Register routes defined in routes.py
    register_error_handlers(app)                        # Configure handlers for custom exceptions
    return app
