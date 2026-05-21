from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import asyncio
from typing import Dict, Any

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.preference import UserPreference

from app.services.dashboard_service import (
    fetch_coin_prices,
    fetch_market_news,
    generate_ai_insight,
    get_daily_meme
)

router = APIRouter(tags=["Dashboard"])

@router.get("/dashboard", response_model=Dict[str, Any])
async def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Fetch user preferences from the database
    preferences = db.query(UserPreference).filter(UserPreference.user_id == current_user.id).first()
    
    if not preferences:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User preferences not found. Please complete the onboarding setup."
        )

    # Use asyncio.gather to fetch all dashboard data concurrently
    prices, news, insight, meme = await asyncio.gather(
        fetch_coin_prices(),
        fetch_market_news(),
        generate_ai_insight(preferences),
        get_daily_meme()
    )

    # Return unified dashboard data
    return {
        "prices": prices,
        "news": news,
        "insight": insight,
        "meme": meme,
        "preferences": {
            "target_assets": preferences.target_assets,
            "investor_persona": preferences.investor_persona,
            "content_preference": preferences.content_preference
        }
    }
