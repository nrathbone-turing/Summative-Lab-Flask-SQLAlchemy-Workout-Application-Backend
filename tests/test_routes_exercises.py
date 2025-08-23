# tests/test_routes_exercises.py
import pytest
from server.models import db, Exercise

def test_list_exercises_returns_all(client, app_context):
    """GET /exercises should return all exercises in the db"""
    e1 = Exercise(name="Push-ups", category="Strength", equipment_needed=False)
    e2 = Exercise(name="Running", category="Cardio", equipment_needed=False)
    db.session.add_all([e1, e2])
    db.session.commit()

    resp = client.get("/exercises/")
    data = resp.get_json()

    assert resp.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    assert any(ex["name"] == "Push-ups" for ex in data)

def test_get_exercise_by_id(client, app_context):
    """GET /exercises/<id> should return the specific exercise"""
    e = Exercise(name="Squats", category="Strength", equipment_needed=True)
    db.session.add(e)
    db.session.commit()

    resp = client.get(f"/exercises/{e.id}")
    data = resp.get_json()

    assert resp.status_code == 200
    assert data["id"] == e.id
    assert data["name"] == "Squats"

def test_get_exercise_not_found(client):
    """GET /exercises/<id> should return 404 if exercise doesn't exist"""
    resp = client.get("/exercises/999")
    assert resp.status_code == 404

def test_create_exercise(client, app_context):
    """POST /exercises should create a new exercise and persist to db"""
    payload = {"name": "Burpees", "category": "Cardio", "equipment_needed": False}
    resp = client.post("/exercises/", json=payload)
    data = resp.get_json()

    assert resp.status_code == 201
    assert data["name"] == "Burpees"

    # confirm persistence
    ex_in_db = Exercise.query.first()
    assert ex_in_db.name == "Burpees"

def test_create_exercise_invalid_payload(client):
    """POST /exercises with missing fields should return 400"""
    resp = client.post("/exercises/", json={})
    assert resp.status_code == 400

def test_delete_exercise(client, app_context):
    """DELETE /exercises/<id> should remove the exercise"""
    e = Exercise(name="Plank", category="Core", equipment_needed=False)
    db.session.add(e)
    db.session.commit()

    resp = client.delete(f"/exercises/{e.id}")
    assert resp.status_code == 204
    assert Exercise.query.get(e.id) is None

def test_delete_exercise_not_found(client):
    """DELETE /exercises/<id> should return 404 if not found"""
    resp = client.delete("/exercises/12345")
    assert resp.status_code == 404