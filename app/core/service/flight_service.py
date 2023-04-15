

from fastapi import HTTPException
from  app.core.dto.flight_prediction_dto import FlightPredictionDto
from app.core.ml.flight_prediction import ml_prediction_flight



class FlightService:
    def prediction(self,input_value):
        if(not(input_value and input_value.strip())):
            
            raise HTTPException(status_code=400,detail="Input_value is required")
        else:
            predicted_value_dto= FlightPredictionDto(input_value,ml_prediction_flight.predict_pipeline(input_value))
            return predicted_value_dto.__dict__
 
flight_service:object = FlightService()














