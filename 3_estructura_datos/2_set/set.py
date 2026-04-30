# un set es un conjunto ordenado de elementos UNICOS. Se utiliza para eliminar elementos duplicados de un conjunto

# esto es una lista no un set
lista = [1,1,1,2,2,2,2,3,3,3,4,4,5,5,5,5,5,5,3,6,7,5,9]
#con set convierte una lista con elementos duplicados en un set sin elementos duplicados
mi_set = set(lista)
print('lista original', lista)
print('conjunto_final', mi_set)
#con list convierte el set otra vez en lista
print('lista final', list(mi_set))

#con las {} creamos un set
frutas = {"manzana", "naranja", "pera", "platano", "pera"}
print(frutas)

#en los sets se puede añadir elementos. Solo de 1 en 1
frutas.add("Melón")
frutas.add("Pera") #si el elemento existe, no lo añade pero no da error
print(frutas)

#borrar elementos de un set con remove
frutas.remove("Melón")#si el elemento no existe o está mal escrito, da error y para el programa
print(frutas)

#borrar elementos de un set con discard
frutas.discard("sandía")#si el elemento no existe o está mal escrito, no da error y no para el programa
print(frutas)

# vaciarlo y eliminarlo
frutas.clear()
print(frutas)
del(frutas) # Eliminaria