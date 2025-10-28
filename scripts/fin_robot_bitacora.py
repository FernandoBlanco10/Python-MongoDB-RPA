import json
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId 

doc_id = GetVar('doc_id')
estatus_fin = GetVar('estatus_fin')
archivo_encontrado = GetVar('archivo_encontrado')

client = MongoClient(GetVar('client'))
db = client[GetVar('db')]
collection = db[GetVar('collection')]

doc_id = ObjectId(doc_id)
fin = datetime.now()
ejecucion = collection.find_one({"_id": doc_id})
inicio = datetime.fromisoformat(ejecucion["inicio"])
duracion = (fin - inicio).total_seconds()

if estatus_fin == "True":
    collection.update_one(
        {"_id": doc_id},
        {"$set": {
            "fin": fin.isoformat(),
            "duracion_segundos": duracion,
            "archivo_encontrado": archivo_encontrado,
            "estado": "OK"
        }}
    )

else:
    collection.update_one(
        {"_id": doc_id},
        {"$set": {
            "fin": fin.isoformat(),
            "duracion_segundos": duracion,
            "estado": "FALLA"
        }}
    )

client.close()