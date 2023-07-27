#Consultar numero total de contactos
import json
def Consultar_numero_contactos(contactos):
    print(f"\n El numero total de contactos es: {len(contactos)}")


#Consultar numero definido de contactos
def consultar_n_contactos(contactos):
    numero = int(input("Ingrese el número de contactos que desea consultar: "))
    print(f"\n=== Consultar los primeros {numero} Contactos ===")
    contactos_limitados = list(contactos.values())[:numero]
    for contacto in contactos_limitados:
        print(json.dumps(contacto)) 
               