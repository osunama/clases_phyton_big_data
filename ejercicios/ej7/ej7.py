   
# trabajamos con modulos separados. modulo principal y secundario

# el fichero se llamará lista_compra.txt
from lib.functions import add_item, show_shoppingcart, delete_shoppingcart


def main():
    menu = """Bienvenido a lista Compra
[1]. Añadir un producto
[2]. Mostrar Lista de la compra
[3]. Borrar lista
[x]. Salir 
    """
    print(menu)
    option = input('Dime que opción quieres: ')
    if option == '1':
        nombre = input('Que producto necesitas: ').strip()
        cantidad = input('Cuantos necesitas: ').strip()
        msg = add_item(nombre, cantidad)
        print(msg)
    elif option == '2':
        msg = show_shoppingcart()
        print(msg)
    elif option == '3':
        msg = delete_shoppingcart()
        print(msg)
    elif option == 'x':
        print('Hasta pronto')
        return 
    main()


main()



main()

