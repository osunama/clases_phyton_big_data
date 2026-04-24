# Realizar una funcion que me permita evaluar si un numero introducido por parametro es par o impar
# 
# # numero = int(input('Dime un número: '))


# def par_impar(numero):
#     if numero == 0:
#         return "0"
#     if numero % 2 == 0:
#         return "Par"
#     if numero % 2 != 0:
#         return "Impar"
# resultado = par_impar(numero)
# print(f"El número es {resultado}")


#resuelto por juanan


# Realizar una funcion que me introduzca un texto y me cuente sus vocales.

def vocales (texto):
    contar_vocales = 0
    texto = texto.lower()
    for i in range(len(texto)):
        if texto[i] == "a" or texto[i] == "á" or texto[i] == "e"  or texto[i] == "é" or texto[i] == "i" or texto[i] == "o"  or texto[i] == "ó" or texto[i] == "u"  or texto[i] == "ú":
            contar_vocales = contar_vocales + 1
    return contar_vocales
        # elif texto[i] == 'e':
        #     contar_vocales += 1
        # elif texto[i] == "i":
        #     contar_vocales = contar_vocales + 1
        # elif texto[i] == "o":
        #     contar_vocales = contar_vocales + 1
        # elif texto[i] == "u":
        #     contar_vocales = contar_vocales + contar_vocales +1
print(vocales("me gusta el"))