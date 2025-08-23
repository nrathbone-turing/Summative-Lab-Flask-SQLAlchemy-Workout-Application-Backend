# server/routes/workout_exercises.py
from flask import Blueprint, request, jsonify

we_bp = Blueprint("workout_exercises", __name__, url_prefix="/workouts")

@we_bp.post("/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_workout_exercise(workout_id, exercise_id):
    return jsonify({"message": f"Add exercise {exercise_id} to workout {workout_id}"}), 201