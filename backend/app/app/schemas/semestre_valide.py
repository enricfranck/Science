from typing import List, Optional, Any

from pydantic import BaseModel


# Shared properties
class SemestreValideBase(BaseModel):
    semestre: Optional[List[str]] = None
    anne: Optional[List[str]] = None


# Properties to receive via API on creation
class SemestreValideCreate(SemestreValideBase):
    num_carte: str
    semestre: List[str]
    anne: List[str]


# Properties to receive via API on update
class SemestreValideUpdate(SemestreValideBase):
    semestre: List[str]
    anne: List[str]


class SemestreValideInDBBase(SemestreValideBase):
    uuid: Optional[Any]

    class Config:
        orm_mode = True


# Additional properties to return via API
class SemestreValide(SemestreValideInDBBase):
    num_carte: Optional[str]


# Additional properties stored in DB
class SemestreValideInDB(SemestreValideInDBBase):
    pass
