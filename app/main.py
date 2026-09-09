from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.images import router as image_router
from app.api.routes.health import router as health_router
from app.core.config import settings


app = FastAPI(
    title="PhrasePic API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(image_router)
app.include_router(health_router)