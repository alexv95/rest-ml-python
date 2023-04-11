
from fastapi import APIRouter


from app.core.service.flight_service import flightService

class FlightRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/flight-prediction",self.flight_prediction,methods=["GET"])
    def flight_prediction(self):
        return flightService.prediction()
        


flight:object = FlightRouter()



        
