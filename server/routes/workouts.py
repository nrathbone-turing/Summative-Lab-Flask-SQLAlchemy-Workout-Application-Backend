# server/routes/workouts.py
"""
PSEUDOCODE WORKOUT ROUTES:
- GET /workouts --> list all workouts
- GET /workouts/<id> --> show single workout (stretch: include reps/sets/duration)
- POST /workouts --> create a workout
- DELETE /workouts/<id> --> delete workout (stretch: also delete related joins)
"""
from flask import Blueprint, request, jsonify

workouts_bp = Blueprint("workouts", __name__, url_prefix="/workouts")

@workouts_bp.get("/")
def list_workouts():
    return jsonify({"message": "List all workouts"}), 200

@workouts_bp.get("/<int:workout_id>")
def get_workout(workout_id):
    return jsonify({"message": f"Get workout {workout_id}"}), 200

@workouts_bp.post("/")
def create_workout():
    return jsonify({"message": "Create workout"}), 201

@workouts_bp.delete("/<int:workout_id>")
def delete_workout(workout_id):
    return jsonify({"message": f"Delete workout {workout_id}"}), 204