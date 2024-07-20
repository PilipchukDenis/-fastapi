#
# from fastapi import FastAPI, Request, Form
# from fastapi.responses import JSONResponse
# from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
# from typing import List
# from sqlalchemy import create_engine, Column, Integer, String, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# DATABASE_URL = "sqlite:///./test.db"
# Base = declarative_base()
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# class Task(Base):
#     __tablename__ = "задачи"
#     id = Column(Integer, primary_key=True, index=True)
#     description = Column(String, index=True)
#     completed = Column(Boolean, default=False)
#
# Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
# templates = Jinja2Templates(directory="шаблоны")
#
# class TaskCreate(BaseModel):
#     description: str
#
# @app.post("/tasks/", response_model=Task)
# def create_task(task: TaskCreate):
#     db = SessionLocal()
#     db_task = Task(description=task.description)
#     db.add(db_task)
#     db.commit()
#     db.refresh(db_task)
#     db.close()
#     return db_task
#
# @app.get("/tasks/", response_model=List[Task])
# def read_tasks():
#     db = SessionLocal()
#     tasks = db.query(Task).all()
#     db.close()
#     return tasks
#
# @app.patch("/tasks/{task_id}")
# def update_task(task_id: int):
#     db = SessionLocal()
#     task = db.query(Task).filter(Task.id == task_id).first()
#     if task:
#         task.completed = not task.completed
#         db.commit()
#         db.refresh(task)
#     db.close()
#     return task
#
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     db = SessionLocal()
#     task = db.query(Task).filter(Task.id == task_id).first()
#     if task:
#         db.delete(task)
#         db.commit()
#     db.close()
#     return {"message": "Задача удалена"}
#
# @app.get("/")
# def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})
#






















# _______________________________________________________________________________________________







#
# from fastapi import FastAPI, Request, Form
# from fastapi.responses import JSONResponse, RedirectResponse
# from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
# from sqlalchemy import create_engine, Column, Integer, String, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
#
# DATABASE_URL = "sqlite:///./test.db"
# Base = declarative_base()
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# class Task(Base):
#     __tablename__ = "tasks"
#     id = Column(Integer, primary_key=True, index=True)
#     description = Column(String, index=True)
#     completed = Column(Boolean, default=False)
#
# Base.metadata.create_all(bind=engine)
#
#
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
#
# class TaskCreate(BaseModel):
#     description: str
#
# @app.post("/tasks/")
# def create_task(description: str = Form(...)):
#     db = SessionLocal()
#     db_task = Task(description=description)
#     db.add(db_task)
#     db.commit()
#     db.refresh(db_task)
#     db.close()
#     return RedirectResponse(url="/", status_code=303)
#
# @app.get("/tasks/", response_model=list)
# def read_tasks():
#     db = SessionLocal()
#     tasks = db.query(Task).all()
#     db.close()
#     return tasks
#
# @app.patch("/tasks/{task_id}")
# def update_task(task_id: int):
#     db = SessionLocal()
#     task = db.query(Task).filter(Task.id == task_id).first()
#     if task:
#         task.completed = not task.completed
#         db.commit()
#         db.refresh(task)
#     db.close()
#     return task
#
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     db = SessionLocal()
#     task = db.query(Task).filter(Task.id == task_id).first()
#     if task:
#         db.delete(task)
#         db.commit()
#     db.close()
#     return {"message": "Задача удалена"}
#
# @app.get("/")
# def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

