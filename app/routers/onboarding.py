from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.preference import UserPreference
from app.schemas.preference import UserPreferenceCreate, UserPreferenceResponse

router = APIRouter(tags=["Onboarding"])

@router.post("/onboarding", response_model=UserPreferenceResponse, status_code=status.HTTP_201_CREATED)
def create_onboarding_preferences(
    preferences: UserPreferenceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if a preference already exists for this user
    existing_preference = db.query(UserPreference).filter(UserPreference.user_id == current_user.id).first()
    if existing_preference:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Onboarding preferences already exist for this user"
        )
    
    new_preference = UserPreference(
        user_id=current_user.id,
        target_assets=preferences.target_assets,
        investor_persona=preferences.investor_persona,
        content_preference=preferences.content_preference
    )
    
    db.add(new_preference)
    db.commit()
    db.refresh(new_preference)
    
    return new_preference
