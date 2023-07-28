""" Proyecto de tener una Agenda de  usuarios"""

import json
import os

import archivo
from  Consultar_numero_Contactos import  Consultar_numero_contactos, consultar_n_contactos
import alta_dato


class Schedule:
    
    def __init__(self, name, last_name, phone, email, street, number_out,
                  number_in, colony, municipio, city, state, country)->None:
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.number_out = number_out
        self.number_in = number_in
        self.colony =  colony
        self.municipio = municipio
        self.city = city
        self.state = state
        self.country = country  
         

    def as_dict_schedule(self):
        return {
                "name": self.name , 
                "last_name": self.last_name,
                "phone": self.phone,  
                "email": self.email,  
                "street": self.street, 
                "number_out": self.number_out,  
                "number_in":self.number_in,  
                "colony": self.colony,   
                "municipio": self.municipio, 
                "city" : self.city, 
                "state": self.state, 
                "country":self.country  
                }
             
          
    def save(self,file_name):
        content=self.as_dict_schedule()
        #print(content)
        
        if not os.path.exists(file_name): 
            try:
                archivo.create_file(file_name,content)     
            except FileExistsError as error:
                print("No se pudo crear el archivo:",error)
        else:    
            archivo.update_file(file_name, content)
                               
    def get_all_agenda(self,file_name):
        """Listar  personas en la agendan de agenda.json"""
        print("entre")
        agenda=archivo.read_file(file_name)
        for u in  agenda:
            agenda=Schedule(**u)
            print( 
        --      "Nombre:", agenda.name , 
                "Apellido: ", agenda.last_name,
                "telefono: ", agenda.phone,  
                "email: ", agenda.email,  
                "calle: ", agenda.street, 
                "number exterior: ", agenda.number_out, 
                "numbero interior: ",agenda.number_in, 
                "colonia: ", agenda.colony, 
                "municipio: ", agenda.municipio, 
                "ciudad: ",agenda.city,
                "estado: ", agenda.state,  
                "country: ", agenda.country)
            
#Menu Principal

print("\t\t......Sistema Control de Agenda...........")
opcion = "1" 
while opcion in ["1","2","3","4","5"]:
    print("Escoge una Opcion:")
    print("1) Dar De Alta una Direccion.")
    print("2) Consultar Contacto")
    print("3) Consultar Número Total de Contactos")
    print("4) Eliminar contacto")
    print("5) Lista Completa de Contactos")
               
    opcion=input("Opción: ")
    if opcion == "1" :
        address = alta_dato.datos()
        schedule=Schedule(address[0],
                         address[1],
                         address[2],
                         address[3],
                         address[4],
                         address[5],
                         address[6],
                         address[7],
                         address[8],
                         address[9],
                         address[10],
                         address[11])                  
        schedule.save("schedule.json") 
    elif opcion == "2":
        print()   
    elif opcion == 3":
        print("estoy en la opcion 3")
        content=archivo.read_file("schedule.json")
        Consultar_numero_contactos(content) 
    elif opcion == 4:
        print()
    elif opcion == 5: 
        print("hola")
        get_all_agenda("schedule.json")             

#user1 = User("Guadalupe","Llamas","lupitallamas","nolose","lupitallt@hotmail.com") 
#user1.save("users.json")
