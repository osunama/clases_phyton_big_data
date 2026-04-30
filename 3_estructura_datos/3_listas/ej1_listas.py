# pedir numeros por pantalla, insertarlos en una lista de numeros, el programa para cuando introduzcamos un letra y dicha letra no estará en la lista.  
# lista_numeros = ['1', '2', '3', '4']
# print(lista_numeros)
# for letra in lista_numeros:
#     print(lista_numeros)
#     if letra == "o":
#         break
# else:
#     print("la letra no está en la lista")

numeros = []
while True:
    entrada = input("Introduce un número: ")
    if not entrada.isdigit():
        break
    # else: #no es necesario en este caso
    numeros.append(int(entrada))

print("Lista de números:", numeros)