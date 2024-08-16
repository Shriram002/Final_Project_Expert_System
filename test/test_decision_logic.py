from backend.app.decision_logic import evaluate_inventory, select_supplier, optimize_transportation

def test_evaluate_inventory():
    assert evaluate_inventory(20, 30) == "Restock Needed"
    assert evaluate_inventory(40, 30) == "Sufficient Inventory"

def test_select_supplier():
    suppliers = [
        {"name": "Supplier A", "cost": 100.0},
        {"name": "Supplier B", "cost": 90.0},
        {"name": "Supplier C", "cost": 110.0},
    ]
    assert select_supplier(suppliers) == "Supplier B"

def test_optimize_transportation():
    options = [
        {"route": "Route A", "time": 10.0},
        {"route": "Route B", "time": 8.0},
        {"route": "Route C", "time": 12.0},
    ]
    assert optimize_transportation(options) == "Route B"
