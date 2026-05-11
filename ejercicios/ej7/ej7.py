# crear un programa en python que me permita hacer una lista de la compra, 
# Un menu con tres opciones
   # [1].Añadir un producto (nombre, cantidad)
   # [2].Mostrar Lista de la compra
   # [3]. Borrar lista
   # [x]. Salir 
   
# trabajamos con modulos separados. modulo principal y secundario

# el fichero se llamará lista_compra.txt
# 

def main():
    menu = """
[1]. Añadir producto
[2]. Mostrar lista
[3]. Borrar lista
[x]. Salir
################################
"""
    print(menu)

option = input("¿Qué quieres hacer:?")
if option == "1":
    producto = input('Introduce producto: ')
    cantidad = input('Introduce cantidad: ')
elif option == "2":
    print("Mostrar lista")
elif option == "3":
    print("Borrar lista")
elif option == "x":
    print("Hasta pronto")
else:
    print("Opción no valida")
   



main()