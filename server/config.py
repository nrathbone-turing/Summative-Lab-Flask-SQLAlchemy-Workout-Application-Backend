"""
PSEUDOCODE CONFIG:
- Define configurations (Dev/Prod/Test)
- Read DATABASE_URI from env with default sqlite
"""
# import os
# class BaseConfig:
# SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///app.db")
# SQLALCHEMY_TRACK_MODIFICATIONS = False
#
# class DevConfig(BaseConfig):
# DEBUG = True
#
# class TestConfig(BaseConfig):
# TESTING = True
# SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"