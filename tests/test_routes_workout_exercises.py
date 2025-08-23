# tests/test_routes_workout_exercises.py
import pytest
from server.app import app

def test_add_workout_exercise_placeholder(client):
    """
    POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
    should exist and return 201 Created for placeholder scaffold
    """
    resp = client.post("/workouts/1/exercises/1/workout_exercises")
    assert resp.status_code == 201
    assert resp.is_json
    assert "message" in resp.get_json()

def test_list_workouts_placeholder(client):
    """GET /workouts should return 200 OK for placeholder scaffold"""
    resp = client.get("/workouts/")
    assert resp.status_code == 200
    assert resp.is_json
    assert "message" in resp.get_json()

def test_list_exercises_placeholder(client):
    """GET /exercises should return 200 OK for placeholder scaffold"""
    resp = client.get("/exercises/")
    assert resp.status_code == 200
    assert resp.is_json
    assert "message" in resp.get_json()