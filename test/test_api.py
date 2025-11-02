from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["message"] == "Hello World"

def test_list_courses_default_pagination():
    r = client.get("/courses/")
    assert r.status_code == 200
    data = r.json()
    assert "items" in data and len(data["items"]) >= 1
    assert data["page"] == 1
    assert data["limit"] == 10

def test_crud_course():
    # create
    r = client.post("/courses/", json={"title": "New Course", "description": "demo"})
    assert r.status_code == 201
    cid = r.json()["id"]

    # read
    r = client.get(f"/courses/{cid}")
    assert r.status_code == 200
    assert r.json()["title"] == "New Course"

    # update
    r = client.put(f"/courses/{cid}", json={"title": "Updated"})
    assert r.status_code == 200
    assert r.json()["title"] == "Updated"

    # delete
    r = client.delete(f"/courses/{cid}")
    assert r.status_code == 204

    # gone
    r = client.get(f"/courses/{cid}")
    assert r.status_code == 404
