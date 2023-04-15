from fastapi import APIRouter
from app.core.service.flight_service import flight_service

from app.core.swagger.flight_response import FlightPredictionResponse

class FlightRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/flight-prediction",self.flight_prediction,methods=["GET"],response_model=FlightPredictionResponse)
    async def flight_prediction(self,value_to_predict:str):
        return flight_service.prediction(value_to_predict)
        


flight_router:object = FlightRouter()



        
