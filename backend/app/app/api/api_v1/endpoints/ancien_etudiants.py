from typing import Any, List
import uuid

from sqlalchemy.sql import schema

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/{schema}", response_model=List[Any])
def read_etudiant_ancienne(*,
    db: Session = Depends(deps.get_db),
    schema: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve etudiant ancienne.
    """
    if crud.user.is_superuser(current_user):
        etudiant = crud.ancien_etudiant.get_all(schema=schema)
    else:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return etudiant


@router.post("/{schema}", response_model=List[Any])
def create_etudiant_ancien(
    *,
    db: Session = Depends(deps.get_db),
    etudiant_in: schemas.EtudiantAncienCreate,
    schema: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new etudiant.
    """
    if crud.user.is_superuser(current_user):
        etudiant = crud.ancien_etudiant.create_etudiant(schema=schema, obj_in=etudiant_in)
    else:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return etudiant


@router.put("/{uuid}{}", response_model=schemas.EtudiantAncien)
def update_etudiant(
    *,
    db: Session = Depends(deps.get_db),
    uuid: str,
    etudiant_in: schemas.EtudiantAncienUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an etudiant.
    """
    role = crud.role.get_by_uuid(db=db, uuid=uuid)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    role = crud.role.update(db=db, db_obj=role, obj_in=role_in)
    return role


@router.get("/by_num/{schema}", response_model=Any)
def read_etudiant_by_num_carte(
    *,
    db: Session = Depends(deps.get_db),
    schema: str,
    num_carte: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get etudiant by num carte.
    """
    etudiant = crud.ancien_etudiant.get_by_num_carte(schema=schema, num_carte=num_carte)
    if not etudiant:
        raise HTTPException(status_code=404, detail="Etudiant not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return etudiant


@router.delete("/{uuid}", response_model=schemas.Role)
def delete_role(
    *,
    db: Session = Depends(deps.get_db),
    uuid: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an role.
    """
    role = crud.role.get_by_uuid(db=db, uuid=uuid)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    role = crud.role.remove_uuid(db=db, uuid=uuid)
    return role
