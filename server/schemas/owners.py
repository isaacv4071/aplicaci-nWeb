from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from database.models import owner

OwnerOutSchema = pydantic_model_creator(owner, name='Owner',exclude=["created_at","modified_at"])

OwnerInSchema = pydantic_model_creator(owner,name='OwnerIn',exclude=["created_at","modified_at","vehicless"])

class UpdateOwner(BaseModel):
    document_type: Optional[str]
    full_name: Optional[str]
    address: Optional[str]
    phone: Optional[str]
    email: Optional[str]