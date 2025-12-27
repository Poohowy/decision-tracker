from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

class Decision(Base):
    __tablename__ = "decision"

    id = Column(Integer, primary_key=True)
    owner_id = Column(
        Integer,
        ForeignKey("user.id"),
        nullable=False,
    )
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    alternatives = Column(String, nullable=True)
    final_decision = Column(String, nullable=False)
    expectations = Column(String, nullable=True)

    owner = relationship(
        "User",
        back_populates="decisions",
    )

    reviews = relationship(
        "DecisionReview",
        back_populates="decision",
        cascade="all, delete-orphan",
    )
