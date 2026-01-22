import leer_gastos
from datetime import date, timedelta


def reporte_gastos():
    gastos = leer_gastos.leer_gastos('gastos.json')
    
    if len(gastos) == 0:
        print('No hay gastos registrados')
        return
    
    print('=============================================')
    print('            Reporte de Gastos                ')
    print('=============================================')
    print('\n1. Calcular total diario')
    print('2. Calcular total semanal')
    print('3. Calcular total mensual')
    print('4. Regresar al menú principal')
    print('=============================================')
    
    try:
        opcion = int(input('Seleccione una opción: '))
    except ValueError:
        print('Debe ingresar un numero')
        return
    except Exception:
        print('Ocurrio un error')
        return
    
    if opcion == 1:
        # Total de HOY
        hoy = str(date.today())
        total = 0
        contador = 0
        
        for g in gastos:
            if g['fecha'] == hoy:
                total += g['monto']
                contador += 1
        
        print('-----')
        print('Total del dia de hoy:', total)
        print('Cantidad de gastos:', contador)
        
    elif opcion == 2:
        # Total de esta SEMANA (últimos 7 días)
        hoy = date.today()
        hace_7_dias = hoy - timedelta(days=7)
        total = 0
        contador = 0
        
        for g in gastos:
            fecha_gasto = g['fecha']
            if str(hace_7_dias) <= fecha_gasto <= str(hoy):
                total += g['monto']
                contador += 1
        
        print('-----')
        print('Total semanal (ultimos 7 dias):', total)
        print('Cantidad de gastos:', contador)
        
    elif opcion == 3:
        # Total de este MES
        hoy = date.today()
        mes_actual = str(hoy.year) + '-' + str(hoy.month).zfill(2)
        total = 0
        contador = 0
        
        for g in gastos:
            if g['fecha'].startswith(mes_actual):
                total += g['monto']
                contador += 1
        
        print('-----')
        print('Total mensual:', total)
        print('Cantidad de gastos:', contador)
        
    elif opcion == 4:
        print('Volviendo al menu')
        
    else:
        print('Opcion no valida')