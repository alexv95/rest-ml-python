import pickle
import re
from pathlib import Path
import pandas as pd

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

with open(f"{BASE_DIR}/finalized_model_logreg-{__version__}.pkl", "rb") as f:
    model_multi = pickle.load(f)

classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]

c_list = [0] * 37
c_list =[c_list]

df = pd.DataFrame(c_list,columns=["OPERA_Aerolineas Argentinas",
"OPERA_Aeromexico",
"OPERA_Air Canada",
"OPERA_Air France",
"OPERA_Alitalia",
"OPERA_American Airlines",
"OPERA_Austral",
"OPERA_Avianca",
"OPERA_British Airways",
"OPERA_Copa Air",
"OPERA_Delta Air",
"OPERA_Gol Trans",
"OPERA_Grupo LATAM",
"OPERA_Iberia",
"OPERA_JetSmart SPA",
"OPERA_K.L.M.",
"OPERA_Lacsa",
"OPERA_Latin American Wings",
"OPERA_Oceanair Linhas Aereas",
"OPERA_Plus Ultra Lineas Aereas",
"OPERA_Qantas Airways",
"OPERA_Sky Airline",
"OPERA_United Airlines",
"TIPOVUELO_I",
"TIPOVUELO_N",
"MES_1",
"MES_2",
"MES_3",
"MES_4",
"MES_5",
"MES_6",
"MES_7",
"MES_8",
"MES_9",
"MES_10",
"MES_11",
"MES_12"])


class MlPredictionFlight:
    def predict_pipeline(self,text):
        text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
        text = re.sub(r"[[]]", " ", text)
        text = text.lower()
        pred = model.predict([text])
        return classes[pred[0]]

    def predict_pipeline_multiparam(self,fecha_vuelo,numero_vuelo,codigo_ciudad_origen,codigo_ciudad_destino,codigo_aerolinea,fecha_operacion,vuelo_operacion,codigo_origen_operacion,codigo_destino_operacion,codigo_aerolinea_operado,dia,mes,ano,dia_nominal,tipo_vuelo,opera,sigla_origen,sigla_destino):
        opera="OPERA_"+opera
        mes="MES_"+str(mes)
        tipo_vuelo="TIPOVUELO_"+tipo_vuelo

        df[opera] = df[opera].replace([0], 1)
        df[mes] = df[mes].replace([0], 1)
        df[tipo_vuelo] = df[tipo_vuelo].replace([0], 1)

        print("El resultado es:", model_multi.predict(df))
        print("El resultado es:", model_multi.predict_proba(df))

        return


ml_prediction_flight:object= MlPredictionFlight()

