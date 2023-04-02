from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_establish_connection():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "educative_data connected!"
