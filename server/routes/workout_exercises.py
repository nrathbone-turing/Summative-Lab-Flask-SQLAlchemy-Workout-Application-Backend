# server/routes/workout_exercises.py
from flask import Blueprint, request, jsonify
from server.models import db, Workout, Exercise, WorkoutExercise
from server.schemas import WorkoutExerciseSchema, WorkoutExerciseCreateSchema
from marshmallow import ValidationError

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
        # Marshmallow schema validations happen here (ranges, required, schema-level rule)
        payload = we_create_schema.load(data)

        # then if we get here & the payload is valid, create the join row
        link = WorkoutExercise(
            workout=workout,
            exercise=exercise,
            **payload,
        )
        db.session.add(link)
        db.session.commit()

    except ValidationError as err:
        # schema validation errors (e.g., negative reps, nothing provided, etc.)
        return jsonify({"errors": err.messages}), 400
    except ValueError as e:
        # model-level @validates errors (e.g., it converts a string or number into an int successfully, but it turns out to be less than 0)
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