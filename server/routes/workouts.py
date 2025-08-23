# server/routes/workouts.py
from flask import Blueprint, jsonify, request
from server.models import db, Workout
from server.schemas import WorkoutSchema, WorkoutCreateSchema

# define a blueprint for workout-related endpoints
workouts_bp = Blueprint("workouts", __name__, url_prefix="/workouts")

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
workout_create_schema = WorkoutCreateSchema()

@workouts_bp.get("/")
def list_workouts():
    """
    GET /workouts/:
    - return all workouts as JSON list
    """
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200

@workouts_bp.get("/<int:id>")
def get_workout(id):
    """
    GET /workouts/<id>:
    - return a single workout or 404 if not found
    """
    workout = db.session.get(Workout, id)
    if not workout:
        return jsonify({"error": "Workout not found"}), 404
    return jsonify(workout_schema.dump(workout)), 200

@workouts_bp.post("/")
def create_workout():
    """
    POST /workouts/:
    - create a new workout
    - expect JSON payload with date + duration_minutes
    - return 400 if missing/invalid
    """
    data = request.get_json() or {}
    try:
        payload = workout_create_schema.load(data)
    except Exception as err:
        return jsonify({"error": str(err)}), 400

    workout = Workout(**payload)
    db.session.add(workout)
    db.session.commit()
    return jsonify(workout_schema.dump(workout)), 201

@workouts_bp.delete("/<int:id>")
def delete_workout(id):
    """
    DELETE /workouts/<id>:
    - delete workout if exists
    - return 404 if not found
    - return 204 on success
    """
    workout = db.session.get(Workout, id)
    if not workout:
        return jsonify({"error": "Workout not found"}), 404
    db.session.delete(workout)
    db.session.commit()
    return "", 204