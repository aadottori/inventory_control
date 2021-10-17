import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status



def get_all_products(db: Session):
    products = db.query(models.Product).all()
    return products


def create_product(request: schemas.Product, db: Session):
    new_product = models.Product(
                        product_name=request.product_name, 
                        product_type=request.product_type, 
                        price=request.price,
                        user_id=request.user_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_single_product(id, db: Session):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not available.")
    return product


def delete_single_product(id, db: Session):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not available.")
    product.delete(synchronize_session=False)
    db.commit()
    return "Done"


def update_single_product(id, request: schemas.Product, db: Session):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not available.")
    product.update(request.dict()) 
    db.commit() 
    return "Update"
