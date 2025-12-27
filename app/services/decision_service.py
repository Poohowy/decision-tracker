from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models import Decision
from app.schemas.decision import DecisionCreate, DecisionRead

def list_decisions(db: Session) -> List[Decision]:
    decisions = (
        db.query(Decision)
        .offset(0)
        .limit(20)
        .all()
    )
    return decisions

def get_decision_by_id(decision_id: int, db: Session) -> Decision:
    decision = db.get(Decision, decision_id)

    if not decision:
        raise HTTPException(
            status_code=404,
            detail="Decision not found",
        )

    return decision

def create_decision(data: DecisionCreate, db: Session) -> Decision:
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