# server/routes/workout_exercises.py
from flask import Blueprint, request, jsonify
from server.models import db, Workout, Exercise, WorkoutExercise

we_bp = Blueprint("workout_exercises", __name__, url_prefix="")

@we_bp.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_workout_exercise(workout_id, exercise_id):
    """
    POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
    - links an exercise to a workout with reps/sets/duration
    """
    workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)

    if not workout or not exercise:
        return jsonify({"error": "Workout or Exercise not found"}), 404

    data = request.get_json() or {}
    try:
        link = WorkoutExercise(
            workout=workout,
            exercise=exercise,
            reps=data.get("reps"),
            sets=data.get("sets"),
            duration_seconds=data.get("duration_seconds"),
        )
        db.session.add(link)
        db.session.commit()
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "id": link.id,
        "workout_id": link.workout_id,
        "exercise_id": link.exercise_id,
        "reps": link.reps,
        "sets": link.sets,
        "duration_seconds": link.duration_seconds,
    }), 201

@we_bp.get("/workout_exercises/<int:id>")
def get_workout_exercise(id):
    link = WorkoutExercise.query.get(id)
    if not link:
        return jsonify({"error": "WorkoutExercise not found"}), 404

    return jsonify({
        "id": link.id,
        "workout_id": link.workout_id,
        "exercise_id": link.exercise_id,
        "reps": link.reps,
        "sets": link.sets,
        "duration_seconds": link.duration_seconds,
    }), 200

@we_bp.delete("/workout_exercises/<int:id>")
def delete_workout_exercise(id):
    link = WorkoutExercise.query.get(id)
    if not link:
        return jsonify({"error": "WorkoutExercise not found"}), 404

    db.session.delete(link)
    db.session.commit()
    return "", 204