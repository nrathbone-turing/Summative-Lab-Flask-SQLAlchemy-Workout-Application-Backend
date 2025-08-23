# tests/test_routes_workouts.py
import pytest
from server.models import db, Workout
from datetime import date

def test_list_workouts_returns_all(client, app_context):
    """
    GET /workouts/:
    - inserts 2 workouts into the test db
    - expects endpoint to return a JSON list of all workouts
    - confirms status=200, list type, correct count, and a known field value
    """
    w1 = Workout(date=date(2025, 1, 1), duration_minutes=30)
    w2 = Workout(date=date(2025, 1, 2), duration_minutes=45)
    db.session.add_all([w1, w2])
    db.session.commit()

    resp = client.get("/workouts/")
    data = resp.get_json()

    assert resp.status_code == 200
    # the response should be a list of dicts
    assert isinstance(data, list)
    # length should match number of inserted rows
    assert len(data) == 2
    assert any(workout["duration_minutes"] == 30 for workout in data)

def test_get_workout_by_id(client, app_context):
    """
    GET /workouts/<id>:
    - inserts a single workout
    - requests it by id
    - confirms JSON response matches persisted values
    """
    w = Workout(date=date(2025, 2, 1), duration_minutes=60)
    db.session.add(w)
    db.session.commit()

    resp = client.get(f"/workouts/{w.id}")
    data = resp.get_json()

    assert resp.status_code == 200
    assert data["id"] == w.id
    assert data["duration_minutes"] == 60

def test_get_workout_not_found(client):
    """
    GET /workouts/<id>:
    - hitting a non-existent id should return 404 error status code
    """
    resp = client.get("/workouts/999")
    assert resp.status_code == 404

def test_create_workout(client, app_context):
    """
    POST /workouts:
    - sends valid JSON payload
    - confirms new workout is created with 201 status code
    - confirms returned data matches input
    - confirms that the data persisted in the db
    """
    payload = {"date": "2025-03-01", "duration_minutes": 40}
    resp = client.post("/workouts/", json=payload)
    data = resp.get_json()

    assert resp.status_code == 201
    assert data["duration_minutes"] == 40

    # confirm persistence
    workout_in_db = Workout.query.first()
    assert workout_in_db.duration_minutes == 40

def test_create_workout_invalid_payload(client):
    """
    POST /workouts/:
    - sends empty JSON payload
    - expects `400 Bad Request` because required fields are missing
    """
    resp = client.post("/workouts/", json={})
    assert resp.status_code == 400

def test_delete_workout(client, app_context):
    """
    DELETE /workouts/<id>:
    - inserts a workout
    - deletes it by id
    - should return a `204 No Content` status code
    - confirms row is removed from db
    """
    w = Workout(date=date(2025, 4, 1), duration_minutes=25)
    db.session.add(w)
    db.session.commit()

    resp = client.delete(f"/workouts/{w.id}")
    assert resp.status_code == 204

    # confirm removed from db
    assert Workout.query.get(w.id) is None

def test_delete_workout_not_found(client):
    """
    DELETE /workouts/<id>:
    - deleting a non-existent workout should also return a 404 status code
    """
    resp = client.delete("/workouts/12345")
    assert resp.status_code == 404