# server/routes/workout_exercises.py
from flask import Blueprint, request, jsonify
from server.models import db, Workout, Exercise, WorkoutExercise
from server.schemas import WorkoutExerciseSchema, WorkoutExerciseCreateSchema

we_bp = Blueprint("workout_exercises", __name__, url_prefix="")

we_schema = WorkoutExerciseSchema()
we_create_schema = WorkoutExerciseCreateSchema()

@we_bp.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_workout_exercise(workout_id, exercise_id):
    """
    POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
    - links an exercise to a workout with reps/sets/duration
    """
    workout = db.session.get(Workout, workout_id)
    exercise = db.session.get(Exercise, exercise_id)
    if not workout or not exercise:
        return jsonify({"error": "Workout or Exercise not found"}), 404

    data = request.get_json() or {}
    try:
        payload = we_create_schema.load(data)  # validates ints / allows None
        link = WorkoutExercise(
            workout=workout,
            exercise=exercise,
            **payload,
        )
        db.session.add(link)
        db.session.commit()
    except ValueError as e:
        # from @validates on the model (negative numbers, etc.)
        return jsonify({"error": str(e)}), 400
    except Exception as err:
        return jsonify({"error": str(err)}), 400

    return jsonify(we_schema.dump(link)), 201

@we_bp.get("/workout_exercises/<int:id>")
def get_workout_exercise(id):
    """GET /workout_exercises/<id> should show join row or return a 404"""
    link = db.session.get(WorkoutExercise, id)
    if not link:
        return jsonify({"error": "WorkoutExercise not found"}), 404
    return jsonify(we_schema.dump(link)), 200

@we_bp.delete("/workout_exercises/<int:id>")
def delete_workout_exercise(id):
    """DELETE /workout_exercises/<id> should return a 204 or a 404"""
    link = db.session.get(WorkoutExercise, id)
    if not link:
        return jsonify({"error": "WorkoutExercise not found"}), 404
    db.session.delete(link)
    db.session.commit()
    return "", 204