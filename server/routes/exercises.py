"""
PSEUDOCODE EXERCISE ROUTES:
- GET /exercises --> list all exercises
- GET /exercises/<id> --> show exercise + associated workouts
- POST /exercises --> create a new exercise
- DELETE /exercises/<id> --> delete an exercise (stretch: also delete related joins)
- POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises → add join row
"""
# from flask import Blueprint, request, jsonify
#
# exercises_bp = Blueprint("exercises", __name__)
#
# @exercises_bp.get("/exercises")
# def list_exercises():
# # PSEUDOCODE: query all exercises; return serialized list
# pass
#
# @exercises_bp.get("/exercises/<int:exercise_id>")
# def get_exercise(exercise_id):
# # PSEUDOCODE: fetch one by id; include associated workouts
# pass
#
# @exercises_bp.post("/exercises")
# def create_exercise():
# # PSEUDOCODE: validate via ExerciseSchema; insert; return created
# pass
#
# @exercises_bp.delete("/exercises/<int:exercise_id>")
# def delete_exercise(exercise_id):
# # PSEUDOCODE: delete exercise
# pass
#
# @exercises_bp.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
# def add_workout_exercise(workout_id, exercise_id):
# # PSEUDOCODE: create WorkoutExercise with reps/sets/duration from JSON
# pass