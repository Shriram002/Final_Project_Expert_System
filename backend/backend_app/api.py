from fastapi import FastAPI, HTTPException
from .decision_logic import evaluate_inventory, select_supplier, optimize_transportation
from .routes import router

app = FastAPI()

app.include_router(router)

@app.post("/evaluate_inventory/")
async def evaluate_inventory_endpoint(inventory_level: int, threshold: int):
    try:
        decision = evaluate_inventory(inventory_level, threshold)
        return {"decision": decision}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/select_supplier/")
async def select_supplier_endpoint(suppliers: list):
    try:
        best_supplier = select_supplier(suppliers)
        return {"best_supplier": best_supplier}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize_transportation/")
async def optimize_transportation_endpoint(options: list):
    try:
        best_route = optimize_transportation(options)
        return {"best_route": best_route}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
