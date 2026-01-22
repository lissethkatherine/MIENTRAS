import json
import os

def leer_gastos(nombre_archivo):

    try:
        if not os.path.exists(nombre_archivo):
            return []
        
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
        
    except json.JSONDecodeError:
        print('archivo dañado')
        return []
    
    except Exception:
        print('Error al leer los gastos')
        return []