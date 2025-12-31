from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Decision(Base):
    __tablename__ = "decision"

    id: Mapped[int] = mapped_column(primary_key=True)

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    alternatives: Mapped[str | None] = mapped_column(String, nullable=True)
    final_decision: Mapped[str] = mapped_column(String, nullable=False)
    expectations: Mapped[str | None] = mapped_column(String, nullable=True)

    owner: Mapped["User"] = relationship(
        back_populates="decisions",
    )

    reviews: Mapped[list["DecisionReview"]] = relationship(
        back_populates="decision",
        cascade="all, delete-orphan",
    )
