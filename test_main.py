from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}


def test_read_phrase():
    response = client.get("/phrase/Family of Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result": ["barack obama", "44th president", "prominent american family"]
    }
