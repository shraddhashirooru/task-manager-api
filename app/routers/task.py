from fastapi import APIRouter,HTTPException,Depends
from app import models, schemas
from app.OAuth2 import get_current_user
from app.database import get_db
from sqlalchemy.orm import Session

router=APIRouter(prefix="/tasks",tags=["Tasks"])


@router.post("/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db:Session=Depends(get_db), user_id:int=Depends(get_current_user)):
    db_task= models.Task(**task.dict(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
@router.get("/", response_model=list[schemas.TaskResponse])
def get_tasks(db:Session=Depends(get_db),user_id:int=Depends(get_current_user)):
    tasks=db.query(models.Task).filter(models.Task.user_id == user_id).all()

    return tasks


@router.get("/{id}", response_model=schemas.TaskResponse)
def get_task(id:int,db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    task = db.query(models.Task).filter(models.Task.user_id == user_id, models.Task.id == id).first()
    if not task:
        raise HTTPException(status_code=403,detail="Task not found or forbidden")
    return task


@router.put("/{id}", response_model=schemas.TaskResponse)
def update_task(id:int, update_task: schemas.TaskUpdate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    task = db.query(models.Task).filter(models.Task.user_id == user_id, models.Task.id == id).first()

    if not task:
        raise HTTPException(status_code=403,detail="Task not found or forbidden")
    if update_task.title:
        task.title=update_task.title
    if update_task.description:
        task.description=update_task.description
    if update_task.status is not None:
        task.status=update_task.status
    db.commit()
    db.refresh(task)
    return task
@router.delete("/{id}")
def delete_task(id:int,db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    task = db.query(models.Task).filter(models.Task.user_id == user_id, models.Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or forbidden")

    db.delete(task)
    db.commit()
    return {"detail": "Task deleted successfully"}
