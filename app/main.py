from fastapi import FastAPI
from app.models import models
from app.db.database import engine
from app.api import routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ClaimPilot360 API")

app.include_router(routes.router)