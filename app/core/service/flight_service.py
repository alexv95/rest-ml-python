

from  app.core.dto.flight_prediction_dto import FlightPredictionDto
from app.core.ml.flight_prediction import mlPredictionFlight

class FlightService:
    def prediction(self,input_value):
        predictedValueDto = FlightPredictionDto(input_value,mlPredictionFlight.predict_pipeline(input_value))
        return predictedValueDto.__dict__
 
flightService:object = FlightService()














