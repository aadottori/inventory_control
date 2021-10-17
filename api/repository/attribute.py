import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status



def get_all_attributes(db: Session):
    attributes = db.query(models.Attribute).all()
    return attributes


def create_attribute(request: schemas.Attribute, db: Session):
    new_attribute = models.Attribute(
                        attribute_name=request.attribute_name, 
                        content=request.content,
                        user_id=request.user_id)
    db.add(new_attribute)
    db.commit()
    db.refresh(new_attribute)
    return new_attribute


def get_single_attribute(id, db: Session):
    attribute = db.query(models.Attribute).filter(models.Attribute.id == id).first()
    if not attribute:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Attribute with id {id} not available.")
    return attribute


def delete_single_attribute(id, db: Session):
    attribute = db.query(models.Attribute).filter(models.Attribute.id == id)
    if not attribute.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Attribute with id {id} not available.")
    attribute.delete(synchronize_session=False)
    db.commit()
    return "Done"


def update_single_attribute(id, request: schemas.Attribute, db: Session):
    attribute = db.query(models.Attribute).filter(models.Attribute.id == id)
    if not attribute.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Attribute with id {id} not available.")
    attribute.update(request.dict()) 
    db.commit() 
    return "Update"
