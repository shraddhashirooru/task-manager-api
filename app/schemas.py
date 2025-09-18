from pydantic import BaseModel,Field,EmailStr
from typing import Union
from datetime import datetime
class TaskBase(BaseModel):
    title:str
    description: str

class TaskCreate(TaskBase):
    status:bool=False

class TaskUpdate(BaseModel):
    title:Union[str,None]=None
    description:Union[str,None]=None
    status:Union[bool,None]=None

class TaskResponse(BaseModel):
    id:int
    title:str
    description:str
    status:bool
    created_at:datetime
    updated_at:datetime
    user_id:int
    model_config = {"from_attributes": True}


class UserBase(BaseModel):
    username:str=Field(...,min_length=3)
    email:EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username:Union[str,None]=None
    email:Union[EmailStr,None]=None
    password:Union[str,None]=None
class UserOut(BaseModel):
    id:int
    username:str
    email:EmailStr

class UserResponse(BaseModel):
    id:int
    username:str
    email:str
    model_config = {"from_attributes":True}
    tasks:list[TaskResponse]

class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:Union[id,None]=None



