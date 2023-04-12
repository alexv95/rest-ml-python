from fastapi import APIRouter
from app.core.service.flight_service import flightService
from app.core.dto.flight_prediction_dto import FlightPredictionDto
from app.core.swagger.flight_response import FlightPredictionResponse
class FlightRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/flight-prediction",self.flight_prediction,methods=["GET"],response_model=FlightPredictionResponse)
    def flight_prediction(self,value_to_predict:str):
        print(value_to_predict);
        return flightService.prediction(value_to_predict)
        


flightRouter:object = FlightRouter()



        
