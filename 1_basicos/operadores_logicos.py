# Atajo para comertar control + Ç

#  un comentario
# otro comentaro

# and, or , not 

precio = float(input('Dime un  precio')) #float para convertirlo a numero
marca = input('Dime una marca: ')

resultado = precio > 100 and marca == "Apple"
print(resultado)

#numero par o divisible por 5
# Pedir numero
# Comprobarlo

numero =  float(input('Dime un numero: '))
# par = numero%2 == 0
# multiplo5 = numero%5 == 0

resultado = numero%2 == 0 or numero%5 == 0
print(resultado)

#Negación

esta_activo = True
print(not esta_activo)