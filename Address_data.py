#- Nombre
#   - Apellido
#    - Teléfono
#    - Correo electrónico
#    - Calle
#    - Número ext
#    - Número int (opcional)
#    - Colonia
#    - Municipio/Alcaldía
#    - Ciudad
#    - Estado
#    - País

'''
Este script crea una tupla con información de cada contacto
'''

answer = input('¿Quieres capturar un contacto? (S/N): ')

if answer == 'S' | answer == 'N':
    name = input('Ingresa tu nombre: ')
    last_name = input('Ingresa tu apellido: ')
    tel = input('Ingresa tu número de teléfono: ')
    email = input('Ingresa tu email: ')
    street = input('Ingresa tu calle: ')
    ext_num = input('Ingresa tu número exterior: ')
    int_num = input('Ingresa tu número interior (opcional): ')
    neighborhood = input('Ingresa tu Colonia: ')
    municipality = input('Ingresa tu Municipio/Alcaldía: ')
    city = input('Ingresa tu Ciudad: ')
    state = input('Ingresa tu Estado: ')
    country = input('Ingresa tu País: ')

else:
    