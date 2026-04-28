## vamos a crear un menu, que me permita decidir que operacion va hacer mi calculadora. 
def pedir_numeros():
    numero1 = float(input("Dime un numero"))
    numero2 = float(input("Dime un numero"))
    resultado = numero1, numero2
def main():
    menu = """
## BIENVENIDO A NUESTRA MARAVILLOSA CALCULADORA ##
--------------------------------------------------
[1] Sumar
[2] Restar
[3] Multiplicar
[x] Salir   
"""
#     print(menu)
#     option = input('¿Que operación quieres realizar? ')
#     if option == '1':
#         numero1 = float(input("Dime un numero"))
#         numero2 = float(input("Dime un numero"))
#         resultado = numero1 + numero2
#         print(resultado)
#     elif option == '2':
#         numero1 = float(input("Dime un numero"))
#         numero2 = float(input("Dime un numero"))
#         resultado = numero1 - numero2
#         print(resultado)
#     elif option == '3':
#         numero1 = float(input("Dime un numero"))
#         numero2 = float(input("Dime un numero"))
#         resultado = numero1 * numero2
#         print(resultado)
#     elif option == 'x':
#         print('Hasta pronto, vuelve cuando quieras')
#     else:
#         print('valor introducido no valido')
#         main()
    
# main()

#como se repite mucho creamos función pedir_numeros y lo sustituimos. Este es el archivo de juanan con codigo optimizado
def main():
    menu = """
## BIENVENIDO A NUESTRA MARAVILLOSA CALCULADORA ##
--------------------------------------------------
[1] Sumar
[2] Restar
[3] Multiplicar
[x] Salir   
"""
    print(menu)
    option = input('¿Que operación quieres realizar? ')
    if option == '1':
        pass
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == 'x':
        print('Hasta pronto, vuelve cuando quieras')
    else:
        print('valor introducido no valido')
    
main()

