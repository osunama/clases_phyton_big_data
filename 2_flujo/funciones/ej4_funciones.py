#Sacar sólo las mayusculas
def = obtener_iniciales(nombre):
    resultado = ""
    for i in range(len(nombre)):
        if i == 0:
            resultado += nombre[i].upper() + "."
        if nombre[i] == " ":
             resultado += nombre[i+1].upper() + "."
