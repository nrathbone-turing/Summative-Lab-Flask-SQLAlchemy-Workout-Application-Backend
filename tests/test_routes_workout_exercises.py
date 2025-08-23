import pytest
from server.app import app

def test_add_workout_exercise_placeholder(client):
    """
    POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
    should exist and return 200/201 status codes based on placeholder scaffolds
    """
    resp = client.post("/workouts/1/exercises/1/workout_exercises")
    assert resp.status_code in (200, 201, 501)  # 501 = Not Implemented (placeholder scaffold)

def test_list_workouts_placeholder(client):
    """GET /workouts should return 200/501 status codes based on placeholder scaffolds"""
    resp = client.get("/workouts")
    assert resp.status_code in (200, 501)   # 501 = Not Implemented (placeholder scaffold)

def test_list_exercises_placeholder(client):
    """GET /exercises should return 200/501 status codes based on placeholder scaffolds"""
    resp = client.get("/exercises")
    assert resp.status_code in (200, 501)
