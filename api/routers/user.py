import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database
from typing import List
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from repository import user


router = APIRouter(
    prefix = "/user",
    tags = ["Users"],
)
get_db = database.get_db




@router.get("/", response_model=List[schemas.ShowUser])
def get_all_users(db: Session = Depends(database.get_db)):
    return user.get_all_users(db)


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get("/{id}", response_model = schemas.ShowUser)
def get_single_user(id:int, db: Session = Depends(get_db)):
    return user.get_single_user(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED) 
def update_single_user(id, request: schemas.User, db: Session = Depends(get_db)):
    return user.update_single_user(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_user(id, db: Session = Depends(get_db)):
    return user.delete_single_user(id, db)


