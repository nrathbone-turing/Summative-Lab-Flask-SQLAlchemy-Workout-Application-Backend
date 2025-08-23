import pytest

def test_healthcheck(client):
    """
    healthcheck route: hitting GET "/" should return a 200 status and a JSON body confirming server status
    """
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}
