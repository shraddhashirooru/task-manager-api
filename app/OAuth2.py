from jose import jwt,JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime,timedelta
from fastapi import HTTPException,Depends

from app.config import settings

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)
def verify_password(plain_password,hashpassword):
    return pwd_context.verify(plain_password,hashpassword)

OAuth2_Scheme=OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY=settings.secret_key
ALGORITHM=settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    exp={"exp":expire}
    to_encode.update(exp)
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
def verify_access_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

def get_current_user(token:str=Depends(OAuth2_Scheme)):
    payload=verify_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401,detail="Could not validate token")

    user_id:int=payload.get("id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")
    return user_id


