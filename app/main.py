from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.models import *
from app.routers import auth, onboarding, dashboard, feedback

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Crypto Advisor Dashboard API",
    description="Backend API for personalized crypto investor dashboard",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for local development with Angular
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(onboarding.router)
app.include_router(dashboard.router)
app.include_router(feedback.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Crypto Advisor Dashboard API!"}
