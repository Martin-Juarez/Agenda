import json

def delete_contact(file_name, id, compair_num=None):
    with open(file_name, 'r') as file:
        data = json.load(file)

    # Utiliza una función de comparación personalizada si se proporciona, o compara los IDs directamente
    if compair_num:
        id_to_delete = [i for i, row in enumerate(data) if compair_num(row['id'], id)]
    else:
        id_to_delete = [i for i, row in enumerate(data) if row['id'] == id]

    if not id_to_delete:
        print("No se encontró ninguna fila con el ID especificado.")
        return

    # Elimina las filas encontradas en orden inverso para evitar cambios en los índices durante el proceso
    for indice in reversed(id_to_delete):
        data.pop(indice)

    with open(file_name, 'w') as archivo:
        json.dump(data, archivo, indent=4)

    print("Se ha eliminado la fila con éxito.")

# Ejemplo de uso:
if __name__ == "__main__":
   # file_name_json = "data.json"
    #id_to_delete = 3  # Aquí puedes utilizar el ID que deseas eliminar, ya sea como string o número (int)

    # Llamada a la función para eliminar por ID
    delete_contact("data.json", 1)
