# quiero un menu cli, 2 opciones insertar contacto y salir
# crear un lista de contactos vacia.
# contactos = []
# en la opcion 1 inserta contacto pedir los datos de contacto, nombre y telefono. E insertarlo en la lista.
# podremos insertar los contactos que queramos antes de salir
# opcion 2: pintar la lista contactos 

# 	Juan Antonio : 9876543
#   ----------------------
#   Miguel Angel: 567899
#   ----------------------

contactos=[]
def pintamos_agenda(lista):
    for contacto in lista:
        print (contacto["nombre"])
        print("__")
        print (contacto['telefono'])
        print("###")
def insertar_contacto(nombre,telefono,lista):
    #crear diccionario
    contacto_nuevo = {
        "nombre": nombre,
        "telefono": telefono
    }
    # añadir diccionario a la lista
    lista.append(contacto_nuevo)
    print(lista)
def main():
    menu = """
    [1]. Insertar contacto
    [2]. Listar contactos
    [3]. Borrar último contacto
    [2]. Listar contactos
    [x]. Salir
    """
    print(menu)
    option = input('Dime que opcion quieres: ')
    if option == "1":
        nombre = input('Nombre: ')
        telefono = input("teléfono: ")
        insertar_contacto(nombre, telefono, contactos)
    elif option == "2":
        pintamos_agenda(contactos)
    elif option == 'x':
        print('Hasta pronto')
        return
    else:
        print('Opcion no valida')

main()