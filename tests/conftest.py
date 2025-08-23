# tests/conftest.py
import os
import pytest

# use an in-memory SQLite db for tests
os.environ["DATABASE_URI"] = "sqlite:///:memory:"

from server.app import app as flask_app
from server.models import db

@pytest.fixture(scope="session")
def app():
    """provide a Flask app instance with app context for the tests"""
    flask_app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    with flask_app.app_context():
        yield flask_app

@pytest.fixture(autouse=True)
def _db(app):
    """provide a fresh database for each test"""
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

@pytest.fixture
def app_context(app):
    """context manager for tests that need to be passed an app context"""
    with app.app_context():
        yield