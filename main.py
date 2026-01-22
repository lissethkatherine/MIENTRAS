from ast import main
import registrar_nuevo_gasto
import listar_gastos
import reporte_gastos


def mostrar_menu():
    print('=============================================')
    print('         Simulador de Gasto Diario          ')
    print('=============================================')
    print('Seleccione una opción:')
    print()
    print('1. Registrar nuevo gasto')
    print('2. Listar gastos')
    print('3. Calcular total de gastos')
    print('4. Generar reporte de gastos')
    print('5. Salir')
    print('=============================================')


while True:
    mostrar_menu()
    
    try:
        opcion = int(input('Ingrese una opción: '))
    except ValueError:
        print('Debe ingresar un numero')
        continue
    except Exception:
        print('Ocurrio un error')
        continue
    
    if opcion == 1:
        registrar_nuevo_gasto.registrar_nuevo_gasto()
    
    elif opcion == 2:
        listar_gastos.listar_gastos()
    
    elif opcion == 3:
        # Calcular total (falta implementar esta función)
        print('Funcion no implementada aun')
    
    elif opcion == 4:
        reporte_gastos.reporte_gastos()
    
    elif opcion == 5:
        print('Saliendo del programa...')
        break
    
    else:
        print('Opcion no valida')
    
if __name__ == "__main__":
    main()