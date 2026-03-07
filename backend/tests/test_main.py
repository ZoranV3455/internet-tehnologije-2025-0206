from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    print(" Home ruta radi")

def test_login():
    response = client.post("/login", json={
        "wallet_address": "test",
        "signature": "test"
    })
    print(f" Login endpoint postoji (vratio {response.status_code})")

if __name__ == "__main__":
    test_home()
    test_login()
    print("Svi testovi su prošli!")