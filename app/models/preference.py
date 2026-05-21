from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # What crypto assets are you interested in? (Stored as comma-separated string or JSON string)
    target_assets = Column(String, nullable=False)
    
    # What type of investor are you? (e.g., HODLer, Day Trader, NFT Collector)
    investor_persona = Column(String, nullable=False)
    
    # What kind of content would you like to see? (e.g., Market News, Charts, Social, Fun)
    content_preference = Column(String, nullable=False)

    # Relationships
    user = relationship("User", back_populates="preference")
