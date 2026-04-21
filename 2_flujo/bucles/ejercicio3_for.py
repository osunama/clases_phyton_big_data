# pedir texto por pantalla de cualquier longitud y  pedir una vocal y decir cuantas vocales tie texto

texto = input("Dame un texto: ").lower()

vocal = input("Dame una vocal: ").lower()

cantidad = len(texto)
numero_vocales = 0

for i in range(cantidad):
    if texto[i] == vocal:
        numero_vocales = numero_vocales +1
print(numero_vocales)


