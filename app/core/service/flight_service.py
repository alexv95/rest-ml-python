

from  app.core.dto.flight_prediction_dto import FlightPredictionDto


class FlightService:
    def prediction(self,input_value):
        predictedValueDto = FlightPredictionDto(input_value,"abc")
        return predictedValueDto.__dict__
 
flightService:object = FlightService()














