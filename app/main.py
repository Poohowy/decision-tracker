from fastapi import FastAPI
from app.routers import health
from app.routers import decisions
from app.routers import reviews
from app.models import User, Decision, DecisionReview

app = FastAPI()
app.include_router(health.router)
app.include_router(decisions.router)
app.include_router(reviews.router)