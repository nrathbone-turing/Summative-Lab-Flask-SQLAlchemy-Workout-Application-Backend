# tests/test_routes_workout_exercises.py
import pytest
from server.models import db, Workout, Exercise, WorkoutExercise
from datetime import date

def test_add_workout_exercise_success(client, app_context):
    """
    POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
    - creates a join row between workout & exercise
    - persists reps/sets data
    """
    # setup parent rows
    w = Workout(date=date(2025, 5, 1), duration_minutes=20)
    e = Exercise(name="Situps", category="Core", equipment_needed=False)
    db.session.add_all([w, e])
    db.session.commit()

    payload = {"reps": 15, "sets": 2}
    resp = client.post(f"/workouts/{w.id}/exercises/{e.id}/workout_exercises", json=payload)
    data = resp.get_json()

    assert resp.status_code == 201
    assert data["workout_id"] == w.id
    assert data["exercise_id"] == e.id
    assert data["reps"] == 15
    assert data["sets"] == 2

    # confirm join row persisted
    link = WorkoutExercise.query.first()
    assert link.reps == 15
    assert link.sets == 2


def test_add_workout_exercise_missing_parents(client, app_context):
    """
    POST join with invalid workout_id/exercise_id should return a 404
    """
    resp = client.post("/workouts/999/exercises/999/workout_exercises", json={"reps": 10})
    assert resp.status_code == 404


def test_add_workout_exercise_invalid_payload(client, app_context):
    """
    POST join with invalid negative values should return a 400
    """
    w = Workout(date=date(2025, 5, 2), duration_minutes=30)
    e = Exercise(name="Plank", category="Core", equipment_needed=False)
    db.session.add_all([w, e])
    db.session.commit()

    resp = client.post(f"/workouts/{w.id}/exercises/{e.id}/workout_exercises", json={"reps": -5})
    assert resp.status_code == 400

def test_delete_workout_exercise_success(client, app_context):
    """
    DELETE /workout_exercises/<id>:
    - should remove the join row and return a 204
    """
    w = Workout(date=date(2025, 6, 1), duration_minutes=20)
    e = Exercise(name="Burpees", category="HIIT", equipment_needed=False)
    db.session.add_all([w, e])
    db.session.commit()

    link = WorkoutExercise(workout=w, exercise=e, reps=5)
    db.session.add(link)
    db.session.commit()

    resp = client.delete(f"/workout_exercises/{link.id}")
    assert resp.status_code == 204
    assert WorkoutExercise.query.get(link.id) is None


def test_delete_workout_exercise_not_found(client):
    """
    DELETE non-existent join should return a 404
    """
    resp = client.delete("/workout_exercises/999")
    assert resp.status_code == 404


def test_get_workout_exercise_success(client, app_context):
    """
    GET /workout_exercises/<id>:
    - should return the join row JSON
    """
    w = Workout(date=date(2025, 6, 2), duration_minutes=25)
    e = Exercise(name="Jump Rope", category="Cardio", equipment_needed=True)
    db.session.add_all([w, e])
    db.session.commit()

    link = WorkoutExercise(workout=w, exercise=e, reps=50, duration_seconds=60)
    db.session.add(link)
    db.session.commit()

    resp = client.get(f"/workout_exercises/{link.id}")
    data = resp.get_json()
    assert resp.status_code == 200
    assert data["id"] == link.id
    assert data["reps"] == 50


def test_get_workout_exercise_not_found(client):
    """
    GET non-existent join should return a 404
    """
    resp = client.get("/workout_exercises/12345")
    assert resp.status_code == 404