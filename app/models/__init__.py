from app.core.database import Base
from app.models.user import User
from app.models.preference import UserPreference
from app.models.feedback import DailyFeedback

# Expose models and Base here for Alembic or to create all tables easily
__all__ = ["Base", "User", "UserPreference", "DailyFeedback"]
