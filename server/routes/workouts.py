# server/routes/workouts.py
"""
WORKOUT ROUTES:
- GET /workouts --> list all workouts
- GET /workouts/<id> --> show single workout
- POST /workouts --> create a workout
- DELETE /workouts/<id> --> delete workout
"""

from flask import Blueprint, jsonify, request
from server.models import db, Workout
from datetime import datetime

# define a blueprint for workout-related endpoints
workouts_bp = Blueprint("workouts", __name__, url_prefix="/workouts")

@workouts_bp.get("/")
def list_workouts():
    """
    GET /workouts/:
    - return all workouts as JSON list
    """
    workouts = Workout.query.all()
    return jsonify([
        {
            "id": w.id,
            "date": w.date.isoformat() if w.date else None,
            "duration_minutes": w.duration_minutes,
            "notes": w.notes,
        }
        for w in workouts
    ]), 200

@workouts_bp.get("/<int:id>")
def get_workout(id):
    """
    GET /workouts/<id>:
    - return a single workout or 404 if not found
    """
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({"error": "Workout not found"}), 404
    return jsonify({
        "id": workout.id,
        "date": workout.date.isoformat() if workout.date else None,
        "duration_minutes": workout.duration_minutes,
        "notes": workout.notes,
    }), 200

@workouts_bp.post("/")
def create_workout():
    """
    POST /workouts/:
    - create a new workout
    - expect JSON payload with date + duration_minutes
    - return 400 if missing/invalid
    """
    data = request.get_json() or {}
    date_str = data.get("date")
    duration = data.get("duration_minutes")

    if not date_str or duration is None:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        workout_date = datetime.fromisoformat(date_str).date()
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    workout = Workout(date=workout_date, duration_minutes=duration, notes=data.get("notes"))
    db.session.add(workout)
    db.session.commit()

    return jsonify({
        "id": workout.id,
        "date": workout.date.isoformat(),
        "duration_minutes": workout.duration_minutes,
        "notes": workout.notes,
    }), 201

@workouts_bp.delete("/<int:id>")
def delete_workout(id):
    """
    DELETE /workouts/<id>:
    - delete workout if exists
    - return 404 if not found
    - return 204 on success
    """
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    db.session.delete(workout)
    db.session.commit()
    return "", 204