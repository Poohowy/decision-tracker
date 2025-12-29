from typing import Optional
from pydantic import BaseModel, Field

class ReviewRead(BaseModel):
    id: int
    decision_id: int
    review: str
    lessons_learned: Optional[str]
    rating: int = Field(min_length=1, max_length=6)

class ReviewCreate(BaseModel):
    decision_id: int
    review: str
    lessons_learned: Optional[str]
    rating: int = Field(min_length=1, max_length=6)
