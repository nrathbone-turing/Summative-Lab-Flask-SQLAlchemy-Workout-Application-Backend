"""
PSEUDOCODE ROUTE TESTS (Workouts):
- GET /workouts returns 200 and list
- GET /workouts/<id> returns 200 and workout (or 404)
- POST /workouts creates record; invalid payload --> 400
- DELETE /workouts/<id> deletes record; not found --> 404
"""
# def test_list_workouts_placeholder(client):
# resp = client.get('/workouts')
# # PSEUDOCODE: assert status code
# assert resp.status_code in (200, 501)