
from fastapi import APIRouter
from app.core.ml.flight_prediction import __version__ as modelVersion



class HealthCheckRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/health-check",self.flight_prediction,methods=["GET"])
    def flight_prediction(self):
        return {"Status":"Ml app is up","Model version": modelVersion}
        


healthCheckRouter:object = HealthCheckRouter()