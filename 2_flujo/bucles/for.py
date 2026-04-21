# for i in range(100):
#     print("Hola" + str(i))
# imprime 100 veces y convierte la función i en string


# imprime 100 veces y con f no hace falta convertir en string
# for i in range(100):
#     print(f'Hola {i}')

#Ejericio pedir numero e imprimir ese numero de veces
# paso 1: almacenar la cantidad de unidades
# paso 2: pedir esa cantidad por pantalla
# paso 3: convertir la unidad en numero
# paso 4: meterla en for
# paso 5: ejecutar el script

numero_veces = int(input('¿Cuántas veces?: '))
print(type(numero_veces))

for i in range(numero_veces):
    print(f'Hola {i}')

print('----------------------------')

# versión 2: elegir punto de inicio y punto final en bucle
for i in range(2, 8):
    print(f'Valor: {i}')

print('----------------------------')

# versión 2: elegir punto de inicio, punto final en bucle y saltos

for i in range(2, 8, 2):
    print(f'Valor con salto de 2 en 2: {i}')


