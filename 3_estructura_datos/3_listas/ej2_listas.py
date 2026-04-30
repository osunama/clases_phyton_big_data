numeros = []

while True:
    numero = input(("Introduce un número: "))
    numero_sin_signo = numero.replace("-","")
    if not numero_sin_signo.isdigit():
        break
    # else: #no es necesario en este caso
    numeros.append(int(numero))

print("Lista de números:", numeros)