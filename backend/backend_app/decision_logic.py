from typing import List

def evaluate_inventory(inventory_level: int, threshold: int) -> str:
    if inventory_level < threshold:
        return "Restock Needed"
    return "Sufficient Inventory"

def select_supplier(suppliers: List[object]) -> str:
    best_supplier = min(suppliers, key=lambda s: s.cost)  # Assuming 'cost' is an attribute
    return best_supplier.name  # Assuming 'name' is an attribute

def optimize_transportation(options: List[object]) -> str:
    best_option = min(options, key=lambda o: o.time)
    return best_option.route
