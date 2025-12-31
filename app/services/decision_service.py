from sqlalchemy import Sequence, select
from sqlalchemy.orm import Session

from app.models import Decision
from app.schemas.decision import DecisionCreate
from app.exceptions.decision import DecisionNotFound

def list_decisions(db: Session) -> Sequence[Decision]:
    stmt = (
        select(Decision)
        .offset(0)
        .limit(20)
    )
    return db.scalars(stmt).all()


def get_decision_by_id(decision_id: int, db: Session) -> type[Decision]:
    decision = db.get(Decision, decision_id)

    if not decision:
        raise DecisionNotFound(decision_id)

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