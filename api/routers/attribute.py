import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from repository import attribute

router = APIRouter(
    prefix = "/attribute",
    tags = ["Attributes"]
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowAttribute])
def get_all_attributes(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return attribute.get_all_attributes(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_attribute(request: schemas.Attribute, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return attribute.create_attribute(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowAttribute)
def get_single_attribute(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return attribute.get_single_attribute(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED) 
def update_single_attribute(id, request: schemas.Attribute, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return attribute.update_single_attribute(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_attribute(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return attribute.delete_single_attribute(id, db)


