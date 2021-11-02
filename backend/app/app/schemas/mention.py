from typing import Optional, Any

from sqlalchemy.dialects.postgresql.base import UUID
from pydantic import BaseModel


# Shared properties
class MentionBase(BaseModel):
    title: Optional[str] = None


# Properties to receive via API on creation
class MentionCreate(MentionBase):
    title: str


# Properties to receive via API on update
class MentionUpdate(MentionBase):
    title: Optional[str] = None


class MentionInDBBase(MentionBase):
    uuid: Optional[Any]

    class Config:
        orm_mode = True


# Additional properties to return via API
class Mention(MentionInDBBase):
    pass


# Additional properties stored in DB
class MentionInDB(MentionInDBBase):
    pass
