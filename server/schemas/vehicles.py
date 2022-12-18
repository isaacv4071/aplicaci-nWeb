from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from database.models import vehicles

VehiclesOutSchema = pydantic_model_creator(
    vehicles, name='Vehicles', exclude=["created_at", "modified_at"])

VehiclesInSchema = pydantic_model_creator(
    vehicles, name='VehiclesIn', exclude=["owner","created_at", "modified_at"])

class UpdateVehicles(BaseModel):
    plate: Optional[str]
    brand: Optional[str]
    model: Optional[str]
    year: Optional[int]
    color: Optional[str]
    owner_id: Optional[str]