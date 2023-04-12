from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.router.flight_router import flightRouter
from app.core.router.health_check import healthCheckRouter
from app.core.swagger.swagger import tags_metadata

def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME,version=1,openapi_tags=tags_metadata)
    _app.include_router(healthCheckRouter.router,tags=["healthcheck"])
    _app.include_router(flightRouter.router,tags=["flight"])
    
    

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
  
    return _app


app = get_application()
