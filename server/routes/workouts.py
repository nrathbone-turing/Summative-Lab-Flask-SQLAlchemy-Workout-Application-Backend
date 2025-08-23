"""
PSEUDOCODE WORKOUT ROUTES:
- GET /workouts --> list all workouts
- GET /workouts/<id> --> show single workout (stretch: include reps/sets/duration)
- POST /workouts --> create a workout
- DELETE /workouts/<id> --> delete workout (stretch: also delete related joins)
"""
# from flask import Blueprint, request, jsonify
#
# workouts_bp = Blueprint("workouts", __name__)
#
# @workouts_bp.get("/workouts")
# def list_workouts():
# # PSEUDOCODE: query all workouts; return serialized list
# pass
#
# @workouts_bp.get("/workouts/<int:workout_id>")
# def get_workout(workout_id):
# # PSEUDOCODE: fetch one by id; optionally include WorkoutExercises
# pass
#
# @workouts_bp.post("/workouts")
# def create_workout():
# # PSEUDOCODE: parse request json via WorkoutSchema; insert; return created
# pass
#
# @workouts_bp.delete("/workouts/<int:workout_id>")
# def delete_workout(workout_id):
# # PSEUDOCODE: delete workout
# pass