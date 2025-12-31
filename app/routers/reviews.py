from typing import List

from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import DecisionReview
from app.schemas.review import ReviewCreate, ReviewRead
from app.services.review_service import list_reviews_for_decision, create_review
from app.exceptions.decision import DecisionNotFound

router = APIRouter(prefix="/decisions")

@router.get("/{decision_id}/reviews", response_model=List[ReviewRead])
def list_reviews_endpoint(
        decision_id: int,
        db: Session = Depends(get_db)
) -> list[DecisionReview]:
    try:
        return list_reviews_for_decision(decision_id=decision_id, db=db)
    except DecisionNotFound as e:
        raise HTTPException(
            status_code=404,
            detail=f"Decision {e} not found"
        )

@router.post("/{decision_id}/reviews", response_model=ReviewRead, status_code=status.HTTP_201_CREATED)
def create_review_endpoint(
        decision_id: int,
        data: ReviewCreate,
        db: Session = Depends(get_db)
) -> DecisionReview:
    try:
        return create_review(
            decision_id=decision_id,
            data=data,
            db=db
        )
    except DecisionNotFound as e:
        raise HTTPException(
            status_code=404,
            detail=f"Decision {e} not found"
        )
