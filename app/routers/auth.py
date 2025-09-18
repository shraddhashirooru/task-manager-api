from fastapi import APIRouter,HTTPException,Depends
from app import models
from app import schemas
from app.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from app.OAuth2 import create_access_token,verify_password
from sqlalchemy.orm import Session


router=APIRouter(tags=["Authentication"])


@router.post("/login", response_model=schemas.Token)
def login_user(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):

    user=db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(form_data.password,user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token=create_access_token({"id":user.id})
    return {"access_token":access_token,"token_type":"Bearer"}