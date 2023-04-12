
from pydantic import BaseModel


class FlightPredictionResponse(BaseModel):
    input_value:str
    predicted_value:str
