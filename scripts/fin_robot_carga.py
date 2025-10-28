import json
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId 

doc_id = GetVar('doc_id_carga')
estatus_fin = GetVar('estatus_fin')
registros_leidos = GetVar('registros_leidos')
registros_cargados = GetVar('registros_cargados')

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
            "registros_leidos": registros_leidos,
            "registros_cargados": registros_cargados,
            "estado": "OK"
        }}
    )

else:
    collection.update_one(
        {"_id": doc_id},
        {"$set": {
            "fin": fin.isoformat(),
            "duracion_segundos": duracion,
            "registros_leidos": registros_leidos,
            "registros_cargados": registros_cargados,
            "estado": "FALLA"
        }}
    )

client.close()