from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.feedback import DailyFeedback
from app.schemas.feedback import FeedbackCreate, FeedbackResponse

router = APIRouter(tags=["Feedback"])

@router.post("/feedback", response_model=FeedbackResponse, status_code=status.HTTP_201_CREATED)
def create_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_feedback = DailyFeedback(
        user_id=current_user.id,
        widget_type=feedback.widget_type,
        is_positive=feedback.is_positive,
        interaction_context=feedback.interaction_context
    )
    
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    
    return new_feedback
