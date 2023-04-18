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
    
  
    async def flight_multiparam(self,
                                fecha_vuelo : str = Query (...,description="Fecha y hora programada del vuelo"),
                                numero_vuelo:int = Query(...,description="Número de vuelo programado", ge=0, le=9999),
                                codigo_ciudad_origen:str =Query(...,description="Código de vuelo de ciudad de origen programado",min_length=3,max_length=5),
                                codigo_ciudad_destino: str = Query(...,description="Código de ciudad de destino programado",min_length=3,max_length=5),
                                codigo_aerolinea: str = Query(...,description="Código aerolínea de vuelo programado",min_length=3,max_length=3),
                                fecha_operacion : str = Query(...,description="Fecha y hora de operación del vuelo"),
                                vuelo_operacion : int = Query(...,description="Número de vuelo de operación del vuelo",ge=10, le=9999),
                                codigo_origen_operacion : str = Query(...,description="Código de ciudad de origen de operación",min_length=3,max_length=5),
                                codigo_destino_operacion :str= Query(...,description="Código de ciudad de destino de operación",min_length=3,max_length=5),
                                codigo_aerolinea_operado : str =Query(...,description="Código aerolínea de vuelo operado",min_length=3,max_length=3),
                                dia : int = Query(...,description="Día del mes de operacion del vuelo",ge=1,le=31),
                                mes :int = Query(...,description="Número del mes de operacion del vuelo",ge=1,le=12),
                                ano: int = Query(...,description = "Año de operacion del vuelo",ge= 2000,le=3000),
                                dia_nominal: str= Query(...,description ="Día de la semana de operación del vuelo",min_length=4,max_length=100),
                                tipo_vuelo : str = Query(...,description="Tipo de vuelo, I =Internacional, N =Nacional",min_lenght=1,max_length=1),
                                opera : str = Query(...,description="Nombre de aerolínea que opera",min_length=4,max_length=100),
                                sigla_origen : str =Query(...,description="Nombre ciudad origen",min_length=3,max_length=100),
                                sigla_destino : str = Query(...,description="Nombre ciudad destino",min_length=4,max_length=100)
                                ):
        return flight_service.prediction_multi(fecha_vuelo,numero_vuelo,codigo_ciudad_origen,codigo_ciudad_destino,codigo_aerolinea,fecha_operacion,vuelo_operacion,codigo_origen_operacion,codigo_destino_operacion,codigo_aerolinea_operado,dia,mes,ano,dia_nominal,tipo_vuelo,opera,sigla_origen,sigla_destino)
        
        


flight_router:object = FlightRouter()



        
