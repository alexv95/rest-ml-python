
from fastapi import APIRouter


class Flight:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/flight-prediction",self.flight_prediction,methods=["GET"])
    def flight_prediction(self):
        return "hello world"
        


flight:object = Flight()



        
