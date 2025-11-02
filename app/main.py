from fastapi import FastAPI
from .routers import courses
from . import db

app = FastAPI(title="Mini Courses API", version="0.1.0")

@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(courses.router)

# seed demo data on startup
@app.on_event("startup")
def _seed():
    db.seed()
