from app.database import Base,engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,TIMESTAMP
from sqlalchemy.sql import func
class User(Base):
    __tablename__="users"

    id=Column(Integer, primary_key=True, index=True)
    username=Column(String,index=True)
    email=Column(String)
    password=Column(String)

    tasks = relationship("Task", back_populates="owner", cascade="all, delete-orphan")

class Task(Base):
    __tablename__="tasks"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    description=Column(String)
    status=Column(Boolean,default=False)
    created_at=Column(TIMESTAMP(timezone=True),server_default=func.now())
    updated_at=Column(TIMESTAMP,server_default=func.now(),onupdate=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="tasks")
Base.metadata.create_all(bind=engine)




