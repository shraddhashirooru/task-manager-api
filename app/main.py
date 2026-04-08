from fastapi import FastAPI
from app.routers import task,user,auth
from app.database import engine
from app import models
app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(task.router)
app.include_router(user.router)
app.include_router(auth.router)










