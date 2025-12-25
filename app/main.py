from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import get_db

app = FastAPI()

@app.get("/health/app")
def health_check():
    return {"status": "ok"}

@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"db": "ok"}