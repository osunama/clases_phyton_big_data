# necesito que pidais varios numeros por pantalla y que los sumeis. El programa termina cuando metemos el numero 0;
# while.
# paso 1: pedir numero constantemente
# paso 2: crear una variables suma = 0
# paso 3: añadir a suma el valor introducido previmente convertido.
# paso 4: pulsando 0 acabamos el ejercicio.
print('#' *40)
print('EJERCICIO SUMA ACUMULADA')
print('#' *40)
print(' ')
numero = float(input('Dime numero: '))
suma = 0

while numero !=0:
    suma += numero
    numero = float(input('Dime numero: '))
print(suma)

# Como lo ha hecho Juanan
suma = 0
while True:
    numero = int(input('Dime numero: '))
    if numero == 0:
        break
    suma += numero
print(suma)
