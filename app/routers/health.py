from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import get_db

from app.db.base import Base

router = APIRouter(prefix="/health")

@router.get("/app")
def health_app():
    return {"status": "ok"}

@router.get("/db")
def health_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok"}

@router.get("/db/tables")
def health_db_tables(db: Session = Depends(get_db)):
    dbkeys = list(Base.metadata.tables.keys())
    return {
        "status": "ok",
        "dbkeys": dbkeys,
    }