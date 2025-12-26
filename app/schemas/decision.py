from typing import Optional
from pydantic import BaseModel, Field

class DecisionRead(BaseModel):
    id: int
    owner_id: int
    title: str
    description: Optional[str] = None
    alternatives: Optional[str] = None
    final_decision: str = None
    expectations: Optional[str] = None

class DecisionCreate(BaseModel):
    owner_id: int
    title: str = Field(min_length=1, max_length=120)
    description: Optional[str] = None
    alternatives: Optional[str] = None
    final_decision: str = None
    expectations: Optional[str] = None

class DecisionUpdate(BaseModel):
    title: Optional[str] = Field(min_length=1, max_length=120)
    description: Optional[str] = None
    alternatives: Optional[str] = None
    final_decision: Optional[str] = None
    expectations: Optional[str] = None
