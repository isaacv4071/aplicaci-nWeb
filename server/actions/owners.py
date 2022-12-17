from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from database.models import owner
from schemas.owners import OwnerOutSchema
from schemas.token import Status
from tortoise.exceptions import DoesNotExist


async def get_owners():
    return await OwnerOutSchema.from_queryset(owner.all())

async def get_owner(document_id) -> OwnerOutSchema:
    return await OwnerOutSchema.from_queryset_single(owner.get(id=document_id))


async def create_owner(owner_new) -> OwnerOutSchema:
    note_dict = owner_new.dict(exclude_unset=True)
    note_obj = await owner.create(**note_dict)
    return await OwnerOutSchema.from_tortoise_orm(note_obj)


async def update_owner(document_id, owner_update) -> OwnerOutSchema:
    try:
        db_note = await OwnerOutSchema.from_queryset_single(owner.get(id=document_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Owner {document_id} not found")

    if db_note.id == document_id:
        await owner.filter(id=document_id).update(**owner_update.dict(exclude_unset=True))
        return await OwnerOutSchema.from_queryset_single(owner.get(id=document_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_owner(document_id) -> Status:  # UPDATED
    try:
        db_note = await OwnerOutSchema.from_queryset_single(owner.get(id=document_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Owner {document_id} not found")

    if db_note.id == document_id:
        deleted_count = await owner.filter(id=document_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Owner {document_id} not found")
        return Status(message=f"Deleted note {document_id}")  # UPDATED

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")