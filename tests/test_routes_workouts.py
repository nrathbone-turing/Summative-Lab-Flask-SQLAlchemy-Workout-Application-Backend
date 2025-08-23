# tests/test_routes_workouts.py
"""
PSEUDOCODE ROUTE TESTS (Workouts):
- GET /workouts returns 200 and list
- GET /workouts/<id> returns 200 and workout (or 404)
- POST /workouts creates record; invalid payload --> 400
- DELETE /workouts/<id> deletes record; not found --> 404
"""

"""
smoke tests for /workouts endpoints to ensure routes are registered and return placeholder 501 status codes for now
"""
def test_list_workouts_placeholder(client):
    resp = client.get("/workouts/")
    assert resp.status_code == 200
    assert resp.is_json
    assert "message" in resp.get_json()

def test_get_workout_placeholder(client):
    resp = client.get("/workouts/1")
    assert resp.status_code == 200
    assert resp.is_json
    assert "message" in resp.get_json()

def test_create_workout_placeholder(client):
    resp = client.post("/workouts/", json={"date": "2025-08-24", "duration_minutes": 30})
    assert resp.status_code == 201
    assert resp.is_json
    assert "message" in resp.get_json()

def test_delete_workout_placeholder(client):
    resp = client.delete("/workouts/1")
    assert resp.status_code == 204
    # 204 status code has no message body, so skiping the json check here

def test_get_workout_not_found(client):
    """GET /workouts/<id> with nonexistent id should return 404"""
    resp = client.get("/workouts/9999")
    assert resp.status_code == 404

def test_create_workout_invalid_payload(client):
    """POST /workouts with missing required field should return 400"""
    resp = client.post("/workouts/", json={})  # no date/duration
    assert resp.status_code == 400

def test_delete_workout_not_found(client):
    """DELETE /workouts/<id> with nonexistent id should return 404"""
    resp = client.delete("/workouts/9999")
    assert resp.status_code == 404