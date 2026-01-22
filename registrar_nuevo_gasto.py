'''Permite al usuario ingresar un nuevo gasto, especificando la cantidad,
categoría (como comida, transporte, etc.) y una breve descripción opcional.
Guarda esta información en un archivo JSON para conservar el registro entre sesiones.'''

from datetime import date
import leer_gastos
import guardar_gastos


def registrar_nuevo_gasto():

    print('=============================================')

    print('       Registrar Nuevo Gasto       ')

    print('=============================================')

    try:
        monto = float (input('- Monto del gasto: '))
    except ValueError:
        print('Debe ingresar solo numeros')
        return
    except Exception:
        print('Ocurrio un error.')
        return

    categoria = input('- Categoría (ej. comida, transporte, entretenimiento, otros):').lower()
    descripcion = input('- Descripción (opcional):')
    fecha = str(date.today())
    print('=============================================')

    opcion = input("Ingrese 'S' para guardar o 'C' para cancelar: ").capitalize()

    if opcion == 'S':

        gastos = leer_gastos.leer_gastos('gastos.json')

        gasto = {
        'monto': monto,
        'categoria': categoria,
        'descripcion': descripcion,
        'fecha': fecha,
       }

        gastos.append(gasto)

        guardar_gastos.guardar_gastos('gastos.json', gastos)
        print('Gasto guardado exitosamente :)')

    elif opcion == 'C':
        print('registro cancelado')
        return
    else:
        print('Opcion no valida')