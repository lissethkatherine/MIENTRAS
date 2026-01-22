'''Listar gastos:
Muestra todos los gastos registrados, con detalles como fecha, categoría, cantidad y descripción

Filtra los gastos por categoría o rango de fechas

(por ejemplo, para ver solo los gastos de "transporte" o solo los del "último mes").'''

import leer_gastos

def listar_gastos():

    gastos = leer_gastos.leer_gastos('gastos.json')

    print("=============================================")

    print("         Listar Gastos         ")

    print("=============================================")

    print("\n1. Ver todos los gastos")

    print("2. Filtrar por categoría")

    print("3. Filtrar por rango de fechas")

    print("4. Regresar al menú principal")

    print("=============================================")

    try:
        opcion = int(input('Seleccione una opción para filtrar los gastos: '))
    except ValueError:
        print('Ddebe ingresar un numero')
    except Exception:

        print('Ocurrio un error inesperado. Intente de nuevo.')
        return

    if opcion == 1:

        for g in gastos:
            print('Monto:', g['monto'])
            print('Categoria:', g['categoria'])
            print('Descripcion:', g['descripcion'])
            print('Fecha:', g['fecha'])
    elif opcion == 2:
        categoria = input('Ingrese la categoria que desea filtar: ').lower()

        contador = 0

        for g in gastos:

            if g['categoria'] == categoria:

                print('Monto:', g['monto'])

                print('Categoria:', g['categoria'])

                print('Descripcion:', g['descripcion'])
                
                print('Fecha:', g['fecha'])

                contador += 1

                if contador == 0:
                    print('No hay gastos en esta categoría')

    elif opcion == 3:
        print('Volviendo al menu')
    else:
        print('Opcion no valida.')