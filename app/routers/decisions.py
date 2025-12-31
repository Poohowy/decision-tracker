from typing import List
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Decision
from app.schemas.decision import DecisionCreate, DecisionRead
from app.services.decision_service import create_decision, get_decision_by_id, list_decisions
from app.exceptions.decision import DecisionNotFound

router = APIRouter(prefix="/decisions")

@router.get("", response_model=List[DecisionRead])
def list_decisions_endpoint(
    db: Session = Depends(get_db)
) -> list[type[Decision]]:
    return list_decisions(db=db)


@router.get("/{decision_id}", response_model=DecisionRead)
def get_decision_by_id_endpoint(
    decision_id: int,
    db: Session = Depends(get_db)
) -> type[Decision]:
    try:
        return get_decision_by_id(decision_id=decision_id, db=db)
    except DecisionNotFound as e:
        raise HTTPException(
            status_code=404,
            detail=f"Decision {e} not found"
        )


@router.post("", response_model=DecisionRead, status_code=status.HTTP_201_CREATED)
def create_decision_endpoint(
    data: DecisionCreate,
    db: Session = Depends(get_db)
) -> Decision:
    return create_decision(data=data, db=db)