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

    
#=============== LIMPIAR VALORES NUMÉRICOS =====================

def limpiar_valor_numerico(valor):

    try:    
        valor = str(valor).strip()
        lista = ["€", "$", "&"]

        for moneda in lista:
            valor = valor.replace(moneda, "")

        valor = valor.replace(".", "")
        valor = valor.replace(",", ".")

        numero = float(valor)

        # Si no tiene decimales → int
        if numero.is_integer():
            return int(numero)

        return numero

    except ValueError:
        return None
    
#=============== ELIMINAR CAMPOS VACIOS =====================
# Si uno de los campos principales está vacio, eliminarlo porque no tiene sentido mantenerlo
def eliminar_vacios(lista, campo_critico):

    for campo in lista[:]:
        if campo[campo_critico] == "":
            lista.remove(campo)


#=============== NORMALIZACIÓN CATEGORÍAS =====================
mapeo_generos = {
    # Rock
    "rock":         "Rock",
    "rokc":         "Rock",
    "roc":          "Rock",
    "rock":         "Rock",
    "ROCK":         "Rock",

    # Electrónica
    "electro":      "Electrónica",
    "electronica":  "Electrónica",
    "Electronica":  "Electrónica",
    "ELECTRONICA":  "Electrónica",
    "Electrónica":  "Electrónica",
    "Electrónic":   "Electrónica",

    # Hip Hop
    "hip hop":      "Hip Hop",
    "hip-hop":      "Hip Hop",
    "Hip Hop":      "Hip Hop",
    "Hip-Hop":      "Hip Hop",
    "HIP HOP":      "Hip Hop",
    "HipHop":       "Hip Hop",

    # Jazz
    "jazz":         "Jazz",
    "Jazz":         "Jazz",
    "JAZZ":         "Jazz",
    "Jaz":          "Jazz",

    # Metal
    "metal":        "Metal",
    "Metal":        "Metal",
    "METAL":        "Metal",
    "Metall":       "Metal",

    # Pop
    "pop":          "Pop",
    "Pop":          "Pop",
    "POP":          "Pop",
    "Ppo":          "Pop",

    # R&B
    "r&b":          "R&B",
    "R&B":          "R&B",
    "R & B":        "R&B",
    "rnb":          "R&B",
    "RnB":          "R&B",

    # Reggaetón
    "reggaeton":    "Reggaetón",
    "Reggaeton":    "Reggaetón",
    "REGGAETON":    "Reggaetón",
    "Reggaetón":    "Reggaetón",
    "regueton":     "Reggaetón",
    "Reguetón":     "Reggaetón",

    # Ska
    "ska":          "Ska",
    "Ska":          "Ska",
    "SKA":          "Ska",

    # Salsa
    "salsa":        "Salsa",
    "Salsa":        "Salsa",
    "SALSA":        "Salsa",

    # Techno
    "techno":       "Techno",
    "Techno":       "Techno",
    "TECHNO":       "Techno",
    "Tekno":        "Techno",

    # Flamenco
    "flamenco":     "Flamenco",
    "Flamenco":     "Flamenco",
    "FLAMENCO":     "Flamenco",
    "Flamenko":     "Flamenco",

    # Folk
    "folk":         "Folk",
    "Folk":         "Folk",
    "FOLK":         "Folk",

    # Indie
    "indie":        "Indie",
    "Indie":        "Indie",
    "INDIE":        "Indie",
    "Indy":         "Indie",

    # Cumbia
    "cumbia":       "Cumbia",
    "Cumbia":       "Cumbia",
    "CUMBIA":       "Cumbia",
    "Kunbia":       "Cumbia",
}

def normalizar_categoria(valor, diccionario_mapeo):
    valor_limpio = valor.lower().strip()
    if valor_limpio in diccionario_mapeo:

        print (diccionario_mapeo[valor_limpio])

    else:

        print(f"AVISO: valor no reconocido → '{valor}'")

        print (valor)

normalizar_categoria("e", mapeo_generos)


# =============== ELIMINAR DUPLICADOS =====================
# Recibe una lista de registros y los campos que identifican
# un registro único. Cuando encuentra dos iguales, conserva
# el más completo (el que tiene menos campos vacíos).

def eliminar_duplicados(datos, campos_clave):

     vistos = {}  # diccionario auxiliar: {clave: registro}

     for registro in datos:

         # Construimos la clave normalizando: minúsculas y sin espacios extra
         # tuple() porque las claves de un diccionario no pueden ser listas
         clave = tuple(str(registro[c]).lower().strip() for c in
campos_clave)

         if clave not in vistos:
             # Primera vez que vemos este registro, lo guardamos
             vistos[clave] = registro

         else:
             # Ya existe uno igual → comparamos cuál es más completo
             # Contamos campos vacíos (None, "", "Sin datos") de cada uno
             vacios_nuevo     = sum(1 for v in registro.values() if not v or v == "Sin datos")
             vacios_existente = sum(1 for v in vistos[clave].values() if not v or v == "Sin datos")

             # Nos quedamos con el que tenga MENOS campos vacíos
             if vacios_nuevo < vacios_existente:
                 vistos[clave] = registro

     return list(vistos.values())


