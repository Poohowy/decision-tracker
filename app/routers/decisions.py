from typing import List
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.decision import DecisionCreate, DecisionRead
from app.services.decision_service import create_decision, get_decision_by_id, list_decisions

router = APIRouter(prefix="/decisions")

@router.get("", response_model=List[DecisionRead])
def list_decisions_endpoint(
    db: Session = Depends(get_db)
) -> List[DecisionRead]:
    return list_decisions(db=db)

@router.get("/{decision_id}", response_model=DecisionRead)
def get_decision_by_id_endpoint(
    decision_id: int,
    db: Session = Depends(get_db)
) -> DecisionRead:
    return get_decision_by_id(decision_id=decision_id, db=db)

@router.post("", response_model=DecisionRead, status_code=status.HTTP_201_CREATED)
def create_decision_endpoint(
    data: DecisionCreate,
    db: Session = Depends(get_db)
) -> DecisionRead:
    return create_decision(data=data, db=db)