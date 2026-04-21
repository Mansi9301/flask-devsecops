import pytest
from app import app, todos

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_todos():
    todos.clear()
    todos.extend([
        {"id": 1, "task": "Buy groceries", "done": False},
        {"id": 2, "task": "Read a book", "done": False},
    ])

def test_get_all_todos(client):
    response = client.get("/todos")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2

def test_get_single_todo(client):
    response = client.get("/todos/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["task"] == "Buy groceries"

def test_get_todo_not_found(client):
    response = client.get("/todos/999")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data

def test_add_todo(client):
    response = client.post("/todos", json={"task": "Go for a walk"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["task"] == "Go for a walk"
    assert data["done"] == False

def test_add_todo_missing_task(client):
    response = client.post("/todos", json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data

def test_add_todo_no_body(client):
    response = client.post("/todos")
    assert response.status_code in [400, 415]

def test_delete_todo(client):
    response = client.delete("/todos/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Todo deleted"

def test_delete_todo_not_found(client):
    response = client.delete("/todos/999")
    assert response.status_code == 404

def test_todo_count_after_add(client):
    client.post("/todos", json={"task": "New task"})
    response = client.get("/todos")
    data = response.get_json()
    assert len(data) == 3

def test_todo_count_after_delete(client):
    client.delete("/todos/1")
    response = client.get("/todos")
    data = response.get_json()
    assert len(data) == 1