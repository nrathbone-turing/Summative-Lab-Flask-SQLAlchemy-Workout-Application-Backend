# tests/test_routes_exercises.py
"""
PSEUDOCODE ROUTE TESTS (Exercises):
- GET /exercises returns 200 and list
- GET /exercises/<id> returns 200 (or 404)
- POST /exercises creates record; invalid payload --> 400
- DELETE /exercises/<id> --> 204/200; not found --> 404
- POST join endpoint adds WorkoutExercise
"""

"""
smoke tests for /exercises endpoints to ensure routes are registered and return placeholder 501 status codes for now
"""

def test_list_exercises_placeholder(client):
    resp = client.get("/exercises/")
    assert resp.status_code == 501
    assert resp.is_json
    assert "message" in resp.get_json()

def test_get_exercise_placeholder(client):
    resp = client.get("/exercises/1")
    assert resp.status_code == 501
    assert resp.is_json
    assert "message" in resp.get_json()

def test_create_exercise_placeholder(client):
    resp = client.post("/exercises/", json={"name": "Push-ups", "category": "Strength"})
    assert resp.status_code == 501
    assert resp.is_json
    assert "message" in resp.get_json()

def test_delete_exercise_placeholder(client):
    resp = client.delete("/exercises/1")
    assert resp.status_code == 501
    assert resp.is_json
    assert "message" in resp.get_json()