"""
PSEUDOCODE APP SETUP:
- Initialize Flask app
- Configure SQLAlchemy + Migrate
- Register blueprints for /workouts and /exercises
- Define placeholder routes or healthcheck
"""
# from flask import Flask, make_response, jsonify
# from flask_migrate import Migrate
# from .models import db
# from .config import DevConfig
# from .routes.workouts import workouts_bp
# from .routes.exercises import exercises_bp
#
# app = Flask(__name__)
# app.config.from_object(DevConfig)
#
# db.init_app(app)
# migrate = Migrate(app, db)
#
# # Register blueprints (prefix at root for exact paths)
# app.register_blueprint(workouts_bp)
# app.register_blueprint(exercises_bp)
#
# @app.get("/")
# def healthcheck():
# # PSEUDOCODE: return a simple message confirming server runs
# return jsonify({"status": "ok"}), 200
#
# if __name__ == "__main__":
# app.run(port=5555, debug=True)

from flask import Flask, make_response
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here

if __name__ == '__main__':
    app.run(port=5555, debug=True)