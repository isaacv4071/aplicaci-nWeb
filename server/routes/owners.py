from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import actions.owners as crud
from auth.jwthandler import get_current_user
from schemas.owners import OwnerOutSchema, OwnerInSchema, UpdateOwner
from schemas.token import Status


router = APIRouter()


@router.get(
    "/owners",
    response_model=List[OwnerOutSchema],
    dependencies=[Depends(get_current_user)],

)
async def get_owners():
    return await crud.get_owners()


@router.get(
    "/owner/{document_id}",
    response_model=OwnerOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_owner(document_id: int) -> OwnerOutSchema:
    try:
        return await crud.get_owner(document_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Owner does not exist",
        )


@router.post("/owners", response_model=OwnerOutSchema, dependencies=[Depends(get_current_user)],)
async def create_owner(owner: OwnerInSchema) -> OwnerOutSchema:
    return await crud.create_owner(owner)


@router.patch(
    "/owner/{document_id}",
    dependencies=[Depends(get_current_user)],
    response_model=OwnerOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_owner(
    document_id: int,
    new_owner: UpdateOwner,
) -> OwnerOutSchema:
    return await crud.update_owner(document_id, new_owner)


@router.delete(
    "/owner/{document_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_owner(
    document_id: int
):
    return await crud.delete_owner(document_id)
