from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class DailyFeedback(Base):
    __tablename__ = "daily_feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Identifies which widget was interacted with (e.g., 'market_news', 'coin_prices', 'ai_insight', 'fun_meme')
    widget_type = Column(String, nullable=False)
    
    # True = Thumbs Up, False = Thumbs Down
    is_positive = Column(Boolean, nullable=False)
    
    # Optional context (e.g., the specific insight text or news ID they gave feedback on)
    interaction_context = Column(String, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="feedbacks")
