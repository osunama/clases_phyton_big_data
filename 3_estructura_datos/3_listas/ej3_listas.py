lista_productos = [('laptop', 1200),('raton', 39),('ram', 200), ('teclado', 10)]

print(lista_productos[3][0])#saca "teclado"

#ordena por orden alfabético
lista_ordenada = sorted(lista_productos)
print(lista_ordenada)

#ordena por precio menor a mayor
lista_ordenada = sorted(lista_productos, key=lambda producto:producto[1])
print(lista_ordenada)

#ordena por precio menor a mayor
lista_ordenada = sorted(lista_productos, key=lambda producto:producto[1], reverse=True)
print(lista_ordenada)

# ordena a los alumnos por altura
alumnos = [('Carlos', 34, 180), ('Lucia', 24, 165), ('Raul', 18, 190), ('Berta', 24, 172)]

lista_altura = sorted(alumnos, key=lambda altura:altura[2], reverse=True)

print(lista_altura)