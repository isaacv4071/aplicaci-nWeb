from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import actions.vehicles as crud
from auth.jwthandler import get_current_user
from schemas.vehicles import VehiclesOutSchema, VehiclesInSchema, UpdateVehicles
from schemas.token import Status


router = APIRouter()


@router.get(
    "/vehicles",
    response_model=List[VehiclesOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_vehicles():
    return await crud.get_vehicles()


@router.get(
    "/vehicle/{plate_id}",
    response_model=VehiclesOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_vehicle(plate_id: str) -> VehiclesOutSchema:
    try:
        return await crud.get_vehicle(plate_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Vehicle does not exist",
        )


@router.post("/vehicles", response_model=VehiclesOutSchema,
             dependencies=[Depends(get_current_user)],
             )
async def create_vehicle(vehicle: VehiclesInSchema) -> VehiclesOutSchema:
    return await crud.create_vehicle(vehicle)


@router.patch(
    "/vehicle/{plate_id}",
    dependencies=[Depends(get_current_user)],
    response_model=VehiclesOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_vehicle(
    plate_id: str,
    new_owner: UpdateVehicles,
) -> VehiclesOutSchema:
    return await crud.update_vehicle(plate_id, new_owner)


@router.delete(
    "/vehicle/{plate_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_vehicle(
    plate_id: str
):
    return await crud.delete_vehicle(plate_id)
