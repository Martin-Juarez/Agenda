'''
Crea un diccionario con la información de Contacto del Cliente
'''
class Address:
    def __init__(self):
        self.name = input('Ingresa tu nombre: ')
        self.last_name = input('Ingresa tu apellido: ')
        self.tel = input('Ingresa tu número de teléfono: ')
        self.email = input('Ingresa tu email: ')
        self.street = input('Ingresa tu calle: ')
        self.ext_num = input('Ingresa tu número exterior: ')
        self.int_num = input('Ingresa tu número interior (opcional): ')
        self.neighborhood = input('Ingresa tu Colonia: ')
        self.municipality = input('Ingresa tu Municipio/Alcaldía: ')
        self.city = input('Ingresa tu Ciudad: ')
        self.state = input('Ingresa tu Estado: ')
        self.country = input('Ingresa tu País: ')

    def as_dict(self):
        if (self.name == "") or (self.last_name == "") or (self.tel == "") or (self.email == "") or (self.street == "") or (self.ext_num == "") or (self.neighborhood == "" or (self.municipality == "") or (self.city == "") or (self.state == "" or (self.country == ""))):
            print("Datos faltantes, vuelve a ingresar los datos.")
        else:
            return { "name" : self.name,
                "last_name" : self.last_name,
                "teléfono" : self.tel,
                "email" : self.email,
                "calle" : self.street,
                "número exterior" : self.ext_num,
                "número interior" : self.int_num,
                "colonia": self.neighborhood,
                "municipio" : self.municipality,
                "city" : self.city,
                "estado" : self.state,
                "pais" : self.country
        }

        
objeto = Address()

print(objeto.as_dict())
print(type(objeto.as_dict()))

