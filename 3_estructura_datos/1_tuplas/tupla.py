#Una tupla es un conjunto de datos inmutable. No se puede cambiar ni de valor ni de longitud. El objetivo es proteger los datos que hay dentro.

mi_primera_tupla = ("Miguel Ángel", 50, True)
frutas = ("naranja", "pera", "platano", "manzana")

print(mi_primera_tupla)
print(frutas)

#como saber longitud tupla
print(len(frutas)) #4

#como sacar un elemento completo.

print(frutas[2]) #platano
print(mi_primera_tupla[0]) #miguel
print(frutas[-2]) #platano

#copiar tupla

otras_frutas = frutas #copiar tupla tal cual
otras_frutas2 = frutas[1:3] #naranja pera

print (frutas[0:3:2])
print (otras_frutas)
print(otras_frutas2)

# uso tipico en el return de las funciones

def devolver_datos_usuario():
    nombre = input('dime un nombre: ')
    edad = input('dime tu edad: ')
    email = input('dime tu email: ')
    return nombre, edad, email
print(devolver_datos_usuario())
#devolver un valor determinado
print(devolver_datos_usuario()[1])

for i in range(0, len(frutas)):
    print(frutas[i])

print('-----------------')

for fruta in frutas:
    print(fruta)

#error con tuplas: reasignar elemento = error. Amentar o disminuir elemento de la tupla
frutas[0] = "Mandarina"

#para eliminar un tupla: #comento para no eliminar la tupla
# del frutas

#para crear una tupla de un único elemento hay que ponerle una , para que lo pinte como tupla. Si no, lo trata como un string
tupla_unico_elemento = ('Juan',)
print(tupla_unico_elemento)