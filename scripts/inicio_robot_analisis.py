import json
from datetime import datetime
from pymongo import MongoClient

bot_name = GetVar('bot_name')

inicio = datetime.now().isoformat()
estado = "Iniciando"

client = MongoClient(GetVar('client'))
db = client[GetVar('db')]
collection = db[GetVar('collection')]

ejecucion = {
    "bot_name": bot_name,
    "inicio": inicio,
    "fin": None,
    "estado": estado,
    "ciudad_mas_ventas": None,
    "duracion_segundos": None
  }

result = collection.insert_one(ejecucion)
doc_id = result.inserted_id

client.close()
  
SetVar('doc_id_analisis',doc_id)