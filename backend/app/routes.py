from fastapi import APIRouter
from .decision_logic import evaluate_inventory, select_supplier, optimize_transportation
from .models import InventoryRequest, SupplierRequest, TransportationRequest

router = APIRouter()

@router.post("/evaluate_inventory/")
async def evaluate_inventory_endpoint(request: InventoryRequest):
    decision = evaluate_inventory(request.inventory_level, request.threshold)
    return {"decision": decision}

@router.post("/select_supplier/")
async def select_supplier_endpoint(request: SupplierRequest):
    best_supplier = select_supplier(request.suppliers)
    return {"best_supplier": best_supplier}

@router.post("/optimize_transportation/")
async def optimize_transportation_endpoint(request: TransportationRequest):
    best_route = optimize_transportation(request.options)
    return {"best_route": best_route}
