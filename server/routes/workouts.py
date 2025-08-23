# server/routes/workouts.py
"""
PSEUDOCODE WORKOUT ROUTES:
- GET /workouts --> list all workouts
- GET /workouts/<id> --> show single workout (stretch: include reps/sets/duration)
- POST /workouts --> create a workout
- DELETE /workouts/<id> --> delete workout (stretch: also delete related joins)
"""
from flask import Blueprint, jsonify

# define a blueprint for workout-related endpoints
workouts_bp = Blueprint("workouts", __name__, url_prefix="/workouts/")

@workouts_bp.get("/")
def list_workouts():
    """
    GET /workouts:
    - intended to return a list of all workouts in the db
    - currently just a placeholder with a 501 Not Implemented status
    """
    return jsonify({"message": "GET /workouts not implemented"}), 501

@workouts_bp.get("/<int:id>")
def get_workout(id):
    """
    GET /workouts/<id>:
    - intended to return a single workout by its id
    - stretch goal: include related WorkoutExercises + exercise info
    - currently just a placeholder with a 501 Not Implemented status
    """
    return jsonify({"message": f"GET /workouts/{id} not implemented"}), 501

@workouts_bp.post("/")
def create_workout():
    """
    POST /workouts:
    - intended to create a new workout from request JSON payload
    - currently just a placeholder with a 501 Not Implemented status
    """
    return jsonify({"message": "POST /workouts not implemented"}), 501

@workouts_bp.delete("/<int:id>")
def delete_workout(id):
    """
    DELETE /workouts/<id>:
    - intended to delete a workout by id
    - stretch goal: also cascade delete associated WorkoutExercises
    - currently just a placeholder with a 501 Not Implemented status
    """
    return jsonify({"message": f"DELETE /workouts/{id} not implemented"}), 501
