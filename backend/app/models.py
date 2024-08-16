from pydantic import BaseModel
from typing import List

class Supplier(BaseModel):
    name: str
    cost: float

class TransportationOption(BaseModel):
    route: str
    time: float

class InventoryRequest(BaseModel):
    inventory_level: int
    threshold: int

class SupplierRequest(BaseModel):
    suppliers: List[Supplier]

class TransportationRequest(BaseModel):
    options: List[TransportationOption]
