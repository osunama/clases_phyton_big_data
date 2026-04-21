# # pintar por pantalla 1000 numeros 
# pero solo los pares. 
# Empezando de 1 hasta 1000. 
# No se puede cambiar los valores iniciales.

for i in range(1, 1000):
    if i % 2 == 0:
        print(i)

# Para impares
for i in range(1, 1000):
    if i % 2 != 0:
        print(i)