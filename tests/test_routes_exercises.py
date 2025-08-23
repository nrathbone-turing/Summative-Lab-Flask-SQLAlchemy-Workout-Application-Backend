"""
PSEUDOCODE ROUTE TESTS (Exercises):
- GET /exercises returns 200 and list
- GET /exercises/<id> returns 200 (or 404)
- POST /exercises creates record; invalid payload --> 400
- DELETE /exercises/<id> --> 204/200; not found --> 404
- POST join endpoint adds WorkoutExercise
"""
# def test_list_exercises_placeholder(client):
# resp = client.get('/exercises')
# # PSEUDOCODE: assert status code
# assert resp.status_code in (200, 501)