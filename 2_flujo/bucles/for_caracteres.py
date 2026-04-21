texto = "Miguel Ángel Osuna"

print(len(texto)) #imprime cantidad de caracteres
print(texto[0]) #imprime la M

for i in range(len(texto)):
    print(texto[i])

# upper # lower
# imprimir solo las mayusculas

for i in range(len(texto)):
    if texto[i] == texto[i].upper():
        print(texto[i])

# imprimir solo las minusculas

for i in range(len(texto)):
    if texto[i] == texto[i].lower():
        print(texto[i])

