

def test_ping_health_check(client):
    response = client.get("/blacklists/ping")
    assert response.status_code == 200
    assert response.data == b"pong"