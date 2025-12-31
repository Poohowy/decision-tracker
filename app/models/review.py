from sqlalchemy import String, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class DecisionReview(Base):
    __tablename__ = "decision_review"

    id: Mapped[int] = mapped_column(primary_key=True)

    decision_id: Mapped[int] = mapped_column(
        ForeignKey("decision.id"),
        nullable=False,
    )

    review: Mapped[str] = mapped_column(String, nullable=False)
    lessons_learned: Mapped[str | None] = mapped_column(String, nullable=True)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)

    decision: Mapped["Decision"] = relationship(
        back_populates="reviews",
    )

    __table_args__ = (
        CheckConstraint(
            "rating BETWEEN 1 AND 6",
            name="ck_rating_value",
        ),
    )
