from pydantic import BaseModel

class UserPreferenceCreate(BaseModel):
    target_assets: str
    investor_persona: str
    content_preference: str

class UserPreferenceResponse(UserPreferenceCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True
        orm_mode = True
