""" Proyecto de tener una Agenda de  usuarios"""

import json
import archivo
import os
#import sus archivos donde esta la funcion de alta, busqueda

class Schedule:
    def __init__(self,id,name,last_name,phone, email,street,number_out,
                 number_in,colony, municipio,city,state,country) -> None:
        self.id = id 
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
                "id" : id, 
        --      "name": self.name , 
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
        content=self.as_dict()
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
        agenda=archivo.read_file(file_name)
        for u in  agenda:
            users=Schedule(**u)
            print("id:", agenda.id, 
        --      "name:", agenda.name , 
                "last_name:", agenda.last_name,
                "phone: ", agenda.phone,  
                "email:", agenda.email,  
                "street:", agenda.street, 
                "number_out:", agenda.number_out, 
                "number_in:",agenda.number_in, 
                "colony:", agenda.colony, 
                "municipio:", agenda.municipio, 
                "city:",agenda.city,
                "state:", agenda.state,  
                "country:", agenda.country)
            
#Menu Principal

print("\t\t......Sistema Control de Agenda...........")
continua = "1" 
while continua in ["1","2"]:
    print("Escoge una Opcion:")
    print("1) Dar De Alta una Direccion.")
    print("2) Concultar un Nombre")           
    opcion=input("Opción: ")
    
if opcion == "1" :
    addrees== alta_dato()
    addrees.save("schedule.json")

#user1 = User("Guadalupe","Llamas","lupitallamas","nolose","lupitallt@hotmail.com") 
#user1.save("users.json")
