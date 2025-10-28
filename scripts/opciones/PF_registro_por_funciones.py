import sys
import os
from bson.objectid import ObjectId

from scripts.opciones.PF_conexion_por_funciones import registrar_bitacora

bot_name = "Bitacora_NoSQL"
estado_inicial = "START"

registrar_bitacora(bot_name,estado_inicial)
doc_id = registrar_bitacora(bot_name,estado_inicial)

# estado_final = "OK"
# finalizar_ejecucion(ObjectId(doc_id), estado_final)