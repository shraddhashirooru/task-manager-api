from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.OAuth2 import hash_password
from app.database import get_db

router=APIRouter(prefix="/users",tags=["Users"])

@router.post('/signup', response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db:Session=Depends(get_db)):
    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists ")

    hashpassword=hash_password(user.password)

    new_user= models.User(username=user.username, email=user.email, password=hashpassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=list[schemas.UserResponse])
def read_users(db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    return users
@router.get("/{id}", response_model=schemas.UserResponse)
def read_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}", response_model=schemas.UserResponse)
def update_user(id:int, update_user: schemas.UserUpdate, db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id).first()


    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if update_user.username:
        existing_user = db.query(models.User).filter(models.User.username == update_user.username,
                                                     models.User.id != id).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        user.username=update_user.username

    if update_user.email:
        user.email=update_user.email
    if update_user.password:
        user.password=hash_password(update_user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{id}")
def delete_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail":"User deleted successfully"}
