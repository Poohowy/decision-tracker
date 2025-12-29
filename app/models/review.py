from sqlalchemy import Column, Integer, String, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

class DecisionReview(Base):
    __tablename__ = "decision_review"

    id = Column(Integer, primary_key=True)
    decision_id = Column(
        Integer,
        ForeignKey("decision.id"),
        nullable=False,
    )
    review = Column(String, nullable=False)
    lessons_learned = Column(String, nullable=True)
    rating = Column(Integer, nullable=False)

    decision = relationship(
        "Decision",
        back_populates="reviews",
    )

    __table_args__ = (
        CheckConstraint("rating BETWEEN 1 AND 6", name="ck_rating_value"),
    )
