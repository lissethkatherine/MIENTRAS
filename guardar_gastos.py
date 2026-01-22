import json

def guardar_gastos(nombre_archivo, datos):

    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4)
    except Exception:
        print('No se pudo guardar los gastos.')