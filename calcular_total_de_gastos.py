import leer_gastos
from datetime import date


def calcular_total():
    gastos = leer_gastos.leer_gastos('gastos.json')

    if len(gastos) == 0:
        print('No hay gastos registrados')
        return

    print('=============================================')
    print('          Calcular Total de Gastos          ')
    print('=============================================')
    print('Seleccione el periodo de cálculo:')
    print()
    print('1. Calcular total diario')
    print('2. Calcular total semanal')
    print('3. Calcular total mensual')
    print('4. Regresar al menú principal')
    print('=============================================')

    try:
        opcion = int(input('Ingrese una opción: '))
    except ValueError:
        print('Debe ingresar un numero')
        return

    if opcion == 1:
        hoy = str(date.today())
        total = 0

        for g in gastos:
            if g['fecha'] == hoy:
                total += g['monto']
        print('Total del dia de hoy:', total)

    elif opcion == 2:
        total = 0
        for g in gastos:
            total += g['monto']
        print('Total semanal:', total)

    elif opcion == 3:
        total = 0
        for g in gastos:
            total += g['monto']
        print('Total mensual:', total)

    elif opcion == 4:
        print('Volviendo al menu principal')

    else:
        print('Opcion no valida')