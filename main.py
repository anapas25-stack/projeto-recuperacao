from fastapi import FastAPI
from database import engine, Base
from routers import cursos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Plataforma de Cursos Online")

app.include_router(cursos.router)