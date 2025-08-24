# server/routes/exercises.py
from flask import Blueprint, request, jsonify
from server.models import db, Exercise
from server.schemas import ExerciseSchema, ExerciseCreateSchema
from marshmallow import ValidationError

exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises/")

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
exercise_create_schema = ExerciseCreateSchema()

@exercises_bp.get("/")
def list_exercises():
    """return all exercises as JSON list"""
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises)), 200

@exercises_bp.get("/<int:exercise_id>")
def get_exercise(exercise_id):
    """return a single exercise by id, or 404 if not found"""
    exercise = db.session.get(Exercise, exercise_id)
    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404
    return jsonify(exercise_schema.dump(exercise)), 200

@exercises_bp.post("/")
def create_exercise():
    """create a new exercise from JSON payload"""
    data = request.get_json() or {}
    try:
        payload = exercise_create_schema.load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as err:
        return jsonify({"error": str(err)}), 400

    exercise = Exercise(**payload)
    db.session.add(exercise)
    db.session.commit()
    return jsonify(exercise_schema.dump(exercise)), 201

@exercises_bp.delete("/<int:exercise_id>")
def delete_exercise(exercise_id):
    """delete an exercise by id, or return 404 if not found"""
    exercise = db.session.get(Exercise, exercise_id)
    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404
    db.session.delete(exercise)
    db.session.commit()
    return "", 204