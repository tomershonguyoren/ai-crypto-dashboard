from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FeedbackCreate(BaseModel):
    widget_type: str
    is_positive: bool
    interaction_context: Optional[str] = None

class FeedbackResponse(FeedbackCreate):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True
