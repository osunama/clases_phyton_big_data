# CREAR UNA VARIABLE EN PYTHON
nombre_alumno = "Miguel Ángel Osuna"
print(nombre_alumno)
print(type(nombre_alumno))

nombre_alumno = 21
print (nombre_alumno)
print(type(nombre_alumno))

# TIPOS BASICOS PYTHON

# NUMÉRICOS
edad = 50
grados = 21
precio = 1299.32

# booleano SIEMPRE LA PRIMERA EN MAYÚSCULA
estado = True
activo = False

# CADENA DE CARACTERES (STRINGS)
nombre = "Sergio"
apellido = 'Osuna' # también comillas simples
mensaje = 'El niño dijo:"Qué pasa"' # uso de comillas dobles y simples
print(mensaje)

# concatenar strings Sergio Osuna 50
nombre_completo = nombre + " " + apellido + ": " + str(edad)
print(nombre_completo)

nombre_completo_2 = f'{nombre} {apellido}: {edad}'
print(nombre_completo_2)

# Multilinea
texto_largo = """
Seleciona:
[1] Sopa
[2] Puré
[3] Gazpacho

"""
print(texto_largo)

opcion = input(texto_largo)
print (f'La opción es {opcion}')