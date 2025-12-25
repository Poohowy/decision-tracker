from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    decisions = relationship(
        "Decision",
        back_populates="owner",
        cascade="all, delete-orphan",
    )
