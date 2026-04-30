nombres = ['Juan', 'Mario', 'Pablo', 'Paula', 'Miriam']

# agregar un unico elemento por el final
nombres.append('Joaquin')
print('append', nombres)

# agregar varios elementos a la vez en una lista por el final
nombres.extend(['Miguel Angel', 'Reniel'])
print('extend', nombres)

# agregar un metodo en cualquier posicion
nombres.insert(3, 'Luis')
print('insert', nombres)

# borrar un elemento de la lista 
# metodo pringle pop()
ultimo_elemento = nombres.pop()
print(nombres)
print(ultimo_elemento)

elemento_tres = nombres.pop(3)
print(elemento_tres)

# eleminar elementos de la lista por contenido
nombres.remove('Mario')
print(nombres)

# funcion que nos permita contar un elemento concreto en la lista.
animales = ["león", "perro", "gato", "jirafa", "león", "hipopótamo"]
print(len(animales)) #6
print(animales.count("leon")) #0
print(animales.count("león")) #2

#invertir una lista. reverse modifica el listado original
animales.reverse()
print(animales)

#ordenar la lista.
numeros = [12,34,5,6,74,34,6,8,1]
letras = ['a', 'F', 'D','i', 'b']

numeros.sort(reverse=True)
print(numeros)

numeros.sort()
print(numeros)
# ordenar sin tener en cuenta mayúsculas ni minusculas
letras.sort(key=str.lower)
print(letras)

#ordenar por longuitud de caracteres


# orden por longitud de caracteres de un string con key=len y con reverse=True se pinta al reves: de mayor nu,mero de caracteres a menor
nombres.sort(key=len, reverse=True)
print(nombres)

# pero sort tiene un problema, modifica la lista original 
# para evitar esto python ha creado un metodo parecido que tiene los mismo parametros. sorted()
nueva_lista = sorted(nombres, key=len , reverse=False)
print(nombres)
print(nueva_lista)