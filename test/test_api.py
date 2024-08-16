import requests

BASE_URL = "http://localhost:8000"

def test_inventory_api():
    response = requests.post(f"{BASE_URL}/evaluate_inventory/", json={
        "inventory_level": 20,
        "threshold": 30
    })
    assert response.status_code == 200
    assert response.json()["decision"] == "Restock Needed"

def test_supplier_api():
    response = requests.post(f"{BASE_URL}/select_supplier/", json={
        "suppliers": [
            {"name": "Supplier A", "cost": 100.0},
            {"name": "Supplier B", "cost": 90.0},
            {"name": "Supplier C", "cost": 110.0},
        ]
    })
    assert response.status_code == 200
    assert response.json()["best_supplier"] == "Supplier B"

def test_transportation_api():
    response = requests.post(f"{BASE_URL}/optimize_transportation/", json={
        "options": [
            {"route": "Route A", "time": 10.0},
            {"route": "Route B", "time": 8.0},
            {"route": "Route C", "time": 12.0},
        ]
    })
    assert response.status_code == 200
    assert response.json()["best_route"] == "Route B"
