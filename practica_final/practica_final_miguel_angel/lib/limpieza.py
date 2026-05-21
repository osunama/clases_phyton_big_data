  #=============== LIMPIAR DATOS =====================
# Elimine espacios al principio y al final (.strip()).
# Elimine espacios dobles o múltiples en medio del texto.
# Devuelva el texto limpio sin cambiar mayúsculas/minúsculas.

def limpiar_texto(valor):
    if not valor:
        return 'Sin datos'
    valor = str(valor).strip() #eliminar espacios por delante y por detrás

    valor = " ".join(valor.split()) #eliminar espacios entre medias

    # if mayusculas:
    #     valor = valor.upper()
    # else:
    #     valor = valor.lower()

    return valor


 #=============== NORMALIZAR TEXTO =====================
#Aplique limpiar_texto primero.
#Convierta el texto a formato estándar (primera letra en mayúscula, resto en minúsculas).
#Corrija tildes que faltan usando el diccionario de correcciones que se proporciona más abajo.

correcciones_tildes = {
    "jose":       "José",      "maria":      "María",
    "garcia":     "García",    "gonzalez":   "González",
    "martinez":   "Martínez",  "lopez":      "López",
    "perez":      "Pérez",     "sanchez":    "Sánchez",
    "gomez":      "Gómez",     "fernandez":  "Fernández",
    "rodriguez":  "Rodríguez", "hernandez":  "Hernández",
    "ramirez":    "Ramírez",   "gutierrez":  "Gutiérrez",
}


def normalizar_texto(texto):
    texto = limpiar_texto(texto)

    palabras = texto.split()

    palabras_tildes = []

    for palabra in palabras:
        if palabra in correcciones_tildes:
            palabras_tildes.append(correcciones_tildes[palabra])
        else:
            palabras_tildes.append(palabra)
    
    texto_corregido = " ".join(palabras_tildes)

    texto_corregido = texto_corregido.title()

    return (texto_corregido)

    

