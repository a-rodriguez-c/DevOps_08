import pytest
from src.main import setup_app
from unittest.mock import patch

@pytest.fixture
def app():
    return setup_app()

@pytest.fixture
def client(app):
    return app.test_client()


