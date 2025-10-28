import json
from datetime import datetime
from pymongo import MongoClient

ruta = GetVar('ruta_configuracion')

# Leer configuración
with open(ruta) as f:
    config = json.load(f)

print("Config cargado:", config)

client = MongoClient(config["mongo_uri"])
db = client[config["database_name"]]
collection = db[config["collection_name"]]

print("Conectado a:", db.name, "| Coleccion:", collection.name)

inicio = datetime.now().isoformat()

SetVar('client',client)
SetVar('db',db)
SetVar('collection',collection)
SetVar('inicio',inicio)