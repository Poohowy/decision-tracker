from fastapi import FastAPI
from app.routers import health
from app.routers import decisions
import app.models

app = FastAPI()
app.include_router(health.router)
app.include_router(decisions.router)
