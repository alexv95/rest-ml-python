from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.router.flight import flight


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.include_router(flight.router)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
  
    return _app


app = get_application()
