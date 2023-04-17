from fastapi import APIRouter,Path, Query
from app.core.service.flight_service import flight_service

from app.core.swagger.flight_response import FlightPredictionResponse
from app.core.swagger.flight_response_codes import flight_responses

class FlightRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/flight-prediction",self.flight_prediction,methods=["GET"],response_model=FlightPredictionResponse)
        self.router.add_api_route("/test",self.flight_multiparam,methods=["GET"],responses={**flight_responses})
    async def flight_prediction(self,value_to_predict:str):
        return flight_service.prediction(value_to_predict)
    
    ##'MES_7', 'TIPOVUELO_I', 'OPERA_Copa Air', 'OPERA_Latin American Wings','MES_12', 'OPERA_Grupo LATAM', 
    # 'MES_10', 'OPERA_JetSmart SPA', 'OPERA_Air Canada',
    ###'MES_9', 'OPERA_American Airlines
    async def flight_multiparam(self,
                                mes_7:int = Query(...,description="Corresponde a si ocurre en el mes 7", ge=0, le=1),
                                tipo_vuelo_i:int = Query(...,description="Corresponde al tipo de vuelo internacional o nacional", ge=0, le=1),
                                opera_copa_air :int = Query(...,description="Corresponde a si lo opera copa air", ge=0, le=1),
                                opera_latin_american_wings:int = Query(...,description="Corresponde a si es operado por latin american airwings", ge=0, le=1),
                                mes_12:int = Query(...,description="Corresponde a si ocurrio en el mes de diciembre", ge=0, le=1),
                                opera_grupo_latam: int = Query(...,description="Corresponde  a si es operado por grupo latam", ge=0, le=1),
                                mes_10 :int = Query(..., description="Corresponde a si ocurre en octubre",ge=0, le=1) ,
                                opera_jet_smart_spa: int = Query(...,description="Corresponde a si es operado por jetsmart", ge=0, le=1),
                                opera_air_canada : int = Query(...,description="Corresponde a si es operado por canada air", ge=0, le=1),
                                mes_9: int = Query(..., description="Corresponde a si ocurre en octubre",ge=0, le=1),
                                opera_american_airlines: int = Query(...,description="Corresponde a si ocurre en american airlines", ge=0, le=1)
                                ):
        return mes_7
        
        


flight_router:object = FlightRouter()



        
