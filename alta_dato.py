"""Pedir los datos"""
import archivo
def datos():

    print('\n\n\n\t\t\t ------Datos------ ')
    address=()
    correcto ='n'
    while correcto not in [ 'S','s', 'Y','y']:   
        name = input('Ingresa tu nombre: ')
        last_name =input('Ingresa tu apellido: ')
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
        
        correcto=input("\t Estan correctos Tus Datos? ")
    
    address = [name,last_name,tel,email,street,ext_num,int_num,neighborhood,
                       municipality,city,state,country]
    #print(address)
    #print(type(address))
    #print (address)
    return address

def serch_name(file_name):
    content= archivo.read_file(file_name)
    id_consultar= input("Ingrese el  id  del contacto que desea consultar: ")
    contacto = file_name.get(id_consultar)
    if contacto:
        print(json.dumps(contacto))
    else:
        print("Contacto no encontrado.")