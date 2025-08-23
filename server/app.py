# server/app.py
"""
PSEUDOCODE APP SETUP:
- Initialize Flask app
- Configure SQLAlchemy + Migrate
- Register blueprints for /workouts and /exercises
- Define placeholder routes or healthcheck
"""
from flask import Flask, jsonify
from flask_migrate import Migrate
from server.models import db
from server.routes.workouts import workouts_bp
from server.routes.exercises import exercises_bp
from server.routes.workout_exercises import we_bp
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "..", "instance", "app.db")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# healthcheck to return a simple message confirming server runs
@app.get("/")
def healthcheck():
    return jsonify({"status": "ok"}), 200

# register blueprints (prefix at root for exact paths)
app.register_blueprint(workouts_bp)
app.register_blueprint(exercises_bp)
app.register_blueprint(we_bp)

if __name__ == '__main__':
    app.run(port=5555, debug=True)