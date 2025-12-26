from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models import Decision
from app.schemas.decision import DecisionCreate, DecisionRead

router = APIRouter(prefix="/decision")

@router.get("", response_model=List[DecisionRead])
def get_decisions(
    db: Session = Depends(get_db)
):
    decisions = (
        db.query(Decision)
        .offset(0)
        .limit(20)
        .all()
    )
    return decisions

@router.get("/{id}", response_model=DecisionRead)
def get_decision(decision_id: int, db: Session = Depends(get_db)):
    decision = db.get(Decision, decision_id)

    if not decision:
        raise HTTPException(
            status_code=404,
            detail="Decision not found",
        )

    return decision

@router.post("", response_model=DecisionRead)
def create_decision(data: DecisionCreate, db: Session = Depends(get_db)):
    decision = Decision(
        owner_id=data.owner_id,
        title=data.title,
        description=data.description,
        alternatives=data.alternatives,
        final_decision=data.final_decision,
        expectations=data.expectations,
    )

    db.add(decision)
    db.commit()
    db.refresh(decision)

    return decision
