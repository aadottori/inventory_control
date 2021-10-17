import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from sqlalchemy.orm import Session
import models, schemas, hashing, jwt_token
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm



def login(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials.")
    if not hashing.Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password.")

    access_token = jwt_token.create_access_token(
        data={"sub": user.email},
    )
    return {"access_token": access_token, "token_type": "bearer"}



