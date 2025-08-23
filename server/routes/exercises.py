# server/routes/exercises.py
from flask import Blueprint, request, jsonify
from server.models import db, Exercise

exercises_bp = Blueprint("exercises", __name__, url_prefix="/exercises/")

@exercises_bp.get("/")
def list_exercises():
    """return all exercises as JSON list"""
    exercises = Exercise.query.all()
    return jsonify([{
        "id": e.id,
        "name": e.name,
        "category": e.category,
        "equipment_needed": e.equipment_needed,
    } for e in exercises]), 200

@exercises_bp.get("/<int:exercise_id>")
def get_exercise(exercise_id):
    """return a single exercise by id, or 404 if not found"""
    exercise = Exercise.query.get(exercise_id)
    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404
    return jsonify({
        "id": exercise.id,
        "name": exercise.name,
        "category": exercise.category,
        "equipment_needed": exercise.equipment_needed,
    }), 200

@exercises_bp.post("/")
def create_exercise():
    """create a new exercise from JSON payload"""
    data = request.get_json() or {}
    name = data.get("name")
    category = data.get("category")
    equipment_needed = data.get("equipment_needed")

    if not name or not category:
        return jsonify({"error": "Missing required fields"}), 400

    exercise = Exercise(
        name=name,
        category=category,
        equipment_needed=bool(equipment_needed),
    )
    db.session.add(exercise)
    db.session.commit()

    return jsonify({
        "id": exercise.id,
        "name": exercise.name,
        "category": exercise.category,
        "equipment_needed": exercise.equipment_needed,
    }), 201

@exercises_bp.delete("/<int:exercise_id>")
def delete_exercise(exercise_id):
    """delete an exercise by id, or return 404 if not found"""
    exercise = Exercise.query.get(exercise_id)
    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    db.session.delete(exercise)
    db.session.commit()
    return "", 204