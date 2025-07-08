# tests/test_task.py
from fastapi.testclient import TestClient
from manage import api  # hoặc app nếu bạn gọi là app

client = TestClient(api)

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200