import logging
from fastapi import FastAPI
from app.core.config import settings
from app.routes import (url_router, user_router)

app = FastAPI()
app.include_router(url_router)
app.include_router(user_router)

logger = logging.getLogger()
logger.info(f'App is running in environment {settings.environment}')
