import json
from datetime import datetime
from pymongo import MongoClient

# Leer configuración
with open("C:/Users/fblanco/Documents/Rocketbot2025/Rocketbot/Bots/Bitacora_NoSQL/config.json") as f:
    config = json.load(f)

print("Config cargado:", config)

client = MongoClient(config["mongo_uri"])
db = client[config["database_name"]]
collection = db[config["collection_name"]]
print("Conectado a:", db.name, "| Coleccion:", collection.name)


def registrar_bitacora(bot_name, estado, registros_procesados=0):
    """
    Inserta un documento con la información de ejecución en MongoDB.
    """
    inicio = datetime.now().isoformat()
    
    ejecucion = {
        "bot_name": bot_name,
        "inicio": inicio,
        "fin": None,
        "estado": estado,
        "registros_procesados": registros_procesados,
        "duracion_segundos": None
    }
    
    result = collection.insert_one(ejecucion)
    return result.inserted_id


def finalizar_ejecucion(doc_id, estado_final="OK"):
    """
    Actualiza la ejecución con tiempo de fin y duración total.
    """
    fin = datetime.now()
    ejecucion = collection.find_one({"_id": doc_id})
    inicio = datetime.fromisoformat(ejecucion["inicio"])
    duracion = (fin - inicio).total_seconds()

    collection.update_one(
        {"_id": doc_id},
        {"$set": {
            "fin": fin.isoformat(),
            "duracion_segundos": duracion,
            "estado": estado_final
        }}
    )