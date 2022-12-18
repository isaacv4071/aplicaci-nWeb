from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from database.models import vehicles
from schemas.vehicles import VehiclesOutSchema
from schemas.token import Status
from tortoise.exceptions import DoesNotExist


async def get_vehicles():
    return await VehiclesOutSchema.from_queryset(vehicles.all())

async def get_vehicle(plate_id) -> VehiclesOutSchema:
    return await VehiclesOutSchema.from_queryset_single(vehicles.get(plate=plate_id))


async def create_vehicle(vehicle_update) -> VehiclesOutSchema:
    vehicle_dict = vehicle_update.dict(exclude_unset=True)
    vehicle_obj = await vehicles.create(**vehicle_dict)
    return await VehiclesOutSchema.from_tortoise_orm(vehicle_obj)


async def update_vehicle(plate_id, vehicle_update) -> VehiclesOutSchema:
    try:
        db_note = await VehiclesOutSchema.from_queryset_single(vehicles.get(plate=plate_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Vehicle {plate_id} not found")

    if db_note.plate == plate_id:
        await vehicles.filter(plate=plate_id).update(**vehicle_update.dict(exclude_unset=True))
        return await VehiclesOutSchema.from_queryset_single(vehicles.get(plate=plate_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_vehicle(plate_id) -> Status:  # UPDATED
    try:
        db_note = await VehiclesOutSchema.from_queryset_single(vehicles.get(plate=plate_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Vehicle {plate_id} not found")

    if db_note.plate == plate_id:
        deleted_count = await vehicles.filter(plate=plate_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Vehicle {plate_id} not found")
        return Status(message=f"Deleted Vehicle {plate_id}")  # UPDATED

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")