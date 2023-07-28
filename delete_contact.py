import json

def delete_contact(file_name, id, compair_num=None):
    with open(file_name, 'r') as file:
        data = json.load(file)

    # compair if emty
    if compair_num:
        id_to_delete = [i for i, row in enumerate(data) if compair_num(row['id'], id)]
    else:
        id_to_delete = [i for i, row in enumerate(data) if row['id'] == id]

    if not id_to_delete:
        print("No se encontró ninguna fila con el ID especificado.")
        return

    # 
    for indice in reversed(id_to_delete):
        data.pop(indice)

    with open(file_name, 'w') as archivo:
        json.dump(data, archivo, indent=4)

    print("Se ha eliminado la fila con éxito.")

# Example:
if __name__ == "__main__":
    delete_contact("data.json", 2)
