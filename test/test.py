import requests

def test_hello_world():
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_health_check():
    response = requests.get("http://localhost:8000/health")
    assert response.status_code == 200
    assert response.json() == {"status":"OK"}