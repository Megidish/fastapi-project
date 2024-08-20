from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_ask_chatgpt():
    response = client.post("/ask-chatgpt/", json={"question": "What is the capital of France?"})
    assert response.status_code == 200
    assert response.json()["answer"] == "Paris"