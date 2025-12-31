from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from app.models import DecisionReview, Decision
from app.schemas.review import ReviewCreate
from app.exceptions.decision import DecisionNotFound


def list_reviews_for_decision(
    decision_id: int,
    db: Session,
) -> Sequence[DecisionReview]:
    decision = db.get(Decision, decision_id)
    if not decision:
        raise DecisionNotFound(decision_id)

    stmt = select(DecisionReview).where(
        DecisionReview.decision_id == decision_id
    )

    return db.scalars(stmt).all()


def create_review(decision_id: int, data: ReviewCreate, db: Session) -> DecisionReview:
    decision = db.get(Decision, decision_id)
    if not decision:
        raise DecisionNotFound(decision_id)

    review = DecisionReview(
        decision_id = decision_id,
        review = data.review,
        lessons_learned = data.lessons_learned,
        rating = data.rating,
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return review