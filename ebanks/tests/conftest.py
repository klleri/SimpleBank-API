import pytest
from simplebank import create_app
from simplebank.config import TestingConfig

@pytest.fixture
def app():
    """
    Creates and configures a new Flask application instance for each test
    """
    app = create_app(config_class=TestingConfig)
    return app

@pytest.fixture
def client(app):
    """
    Provides a Flask test client for the application instance
    """
    # Fornece um test_client do Flask
    return app.test_client()
