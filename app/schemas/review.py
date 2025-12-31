from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class ReviewRead(BaseModel):
    id: int
    decision_id: int
    review: str
    lessons_learned: Optional[str] = None
    rating: int = Field(ge=1, le=6)
    created_at: datetime

    model_config = {"from_attributes": True}

class ReviewCreate(BaseModel):
    review: str
    lessons_learned: Optional[str] = None
    rating: int = Field(ge=1, le=6)
