from typing import Optional, Any
from uuid import uuid4

from sqlalchemy.sql.sqltypes import String

from pydantic import BaseModel, EmailStr


# Shared properties
class EtudiantBase(BaseModel):
    uuid: Optional[Any]
    nom: Optional[str] = None
    prenom: Optional[str] = None
    date_naiss: Optional[str] = None
    lieu_naiss: Optional[str] = None
    adresse: Optional[str] = None
    sexe: Optional[str] = None
    nation: Optional[str] = None
    num_cin: Optional[str] = None
    date_cin: Optional[str] = None
    lieu_cin: Optional[str] = None
    montant: Optional[str] = None
    bacc: Optional[str] = None
    etat: Optional[str] = None
    photo: Optional[str] = None
    num_quitance: Optional[str] = None
    date_quitance: Optional[str] = None
    uuid_mention: Optional[str] = True
    uuid_parcours: Optional[str]


# Properties to receive via API on creation
class EtudiantAncienCreate(EtudiantBase):
    num_carte: str
    nom: str
    prenom: str
    date_naiss: str
    lieu_naiss: str
    adresse: str
    sexe: str
    nation: str
    num_cin: str
    date_cin: str
    lieu_cin: str
    montant: str
    moyenne: str
    bacc: str
    etat: str
    photo: str
    num_quitance: str
    date_quitance: str
    uuid_mention: str
    uuid_parcours: str
    uuid_semestre_petit: str
    uuid_semestre_grand: str


# Properties to receive via API on update
class EtudiantAncienUpdate(EtudiantBase):
    moyenne: Optional[str] = None
    uuid_semestre_petit: Optional[Any]
    uuid_semestre_grand: Optional[Any]


class EtudiantAncienInDBBase(EtudiantBase):
    uuid: Optional[Any]
    num_carte: Optional[str]
    moyenne: Optional[str] = None
    uuid_semestre_petit: Optional[Any]
    uuid_semestre_grand: Optional[Any]

    class Config:
        orm_mode = True


# Additional properties to return via API
class EtudiantAncien(EtudiantAncienInDBBase):
    pass


# Additional properties stored in DB
class EtudiantAncienInDB(EtudiantAncienInDBBase):
    pass
