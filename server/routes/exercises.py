# server/routes/exercises.py
"""
PSEUDOCODE EXERCISE ROUTES:
- GET /exercises --> list all exercises
- GET /exercises/<id> --> show exercise + associated workouts
- POST /exercises --> create a new exercise
- DELETE /exercises/<id> --> delete an exercise (stretch: also delete related joins)
- POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises → add join row
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from flask import Blueprint, request, jsonify

exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises/")

@exercises_bp.get("/")
def list_exercises():
    return jsonify({"message": "List all exercises"}), 200

@exercises_bp.get("/<int:exercise_id>")
def get_exercise(exercise_id):
    return jsonify({"message": f"Get exercise {exercise_id}"}), 200

@exercises_bp.post("/")
def create_exercise():
    return jsonify({"message": "Create exercise"}), 201

@exercises_bp.delete("/<int:exercise_id>")
def delete_exercise(exercise_id):
    return jsonify({"message": f"Delete exercise {exercise_id}"}), 204