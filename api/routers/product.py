import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from repository import product

router = APIRouter(
    prefix = "/product",
    tags = ["Products"]
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowProduct])
def get_all_products(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return product.get_all_products(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(request: schemas.Product, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return product.create_product(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowProduct)
def get_single_product(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return product.get_single_product(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED) 
def update_single_product(id, request: schemas.Product, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return product.update_single_product(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_product(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return product.delete_single_product(id, db)


