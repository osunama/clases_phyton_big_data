# *numeros representa un conjuto de datos, ese conjunto tiene posicion empezando en 0 y acaban n-1 siendo n la longitud o cantidad 
#así se recorre
def sumar (*numeros):
    for i in range(len(numeros)):
        print (numeros[i])
    print("-------------")

sumar (1,2)
sumar (1,2,6)
sumar (1,2,3,8,50)

#asi se suma
def sumar2 (*numeros):
    resultado = 0
    for i in range(len(numeros)):
        resultado += numeros[i]
    print (resultado)
    print("-------------")

sumar2 (1,2)
sumar2 (1,2,6)
sumar2 (1,2,3,8,50)

## hayar media
### media(1,2,3,4,5)
### media(2,3,4)

def media (*numeros):
    resultado = 0
    for i in range(len(numeros)):
        resultado += numeros[i] 
    print (resultado / len(numeros))

media(1,2,3,4,5)
media(2,3,64)

## bucle mas sencillo para manejar listas

def media (*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    print (suma / len(numeros))

media(1,2,3,4,5)
media(2,3,64)