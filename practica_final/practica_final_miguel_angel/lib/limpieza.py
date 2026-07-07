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
        valor = valor.replace("-", "")
        valor = valor.replace("99999", "99")

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
    "Rokc":         "Rock",
    "Roc":         "Rock",
    "roc":          "Rock",
    "rock":         "Rock",
    "ROCK":         "Rock",
    "Rock":         "Rock",

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
    "hiphop":       "Hip Hop",

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
    valor_limpio = valor.strip()
    if valor_limpio in diccionario_mapeo:

       return diccionario_mapeo[valor_limpio]

    else:

        print(f"AVISO: valor no reconocido → '{valor}'")

        return valor
    
# ============================================================
# NORMALIZAR PAISES
# ============================================================
mapeo_paises = {
    # España
    "España":       "España",
    "España ":      "España",
    " España":      "España",
    "ESPAÑA":       "España",
    "españa":       "España",
    "Espana":       "España",

    # Argentina
    "Argentina":    "Argentina",
    "ARGENTINA":    "Argentina",
    "argentina":    "Argentina",
    "Argetina":     "Argentina",

    # Brasil
    "Brasil":       "Brasil",
    "BRASIL":       "Brasil",
    "brasil":       "Brasil",
    "Brazil":       "Brasil",

    # Chile
    "Chile":        "Chile",
    "CHILE":        "Chile",
    "chile":        "Chile",

    # Colombia
    "Colombia":     "Colombia",
    "COLOMBIA":     "Colombia",
    "colombia":     "Colombia",
    "Kolombia":     "Colombia",

    # Cuba
    "Cuba":         "Cuba",
    "CUBA":         "Cuba",
    "cuba":         "Cuba",

    # Estados Unidos
    "EE.UU.":           "Estados Unidos",
    "Estados Unidos":   "Estados Unidos",
    "estados unidos":   "Estados Unidos",
    "USA":              "Estados Unidos",
    "US":               "Estados Unidos",

    # Francia
    "Francia":      "Francia",
    "FRANCIA":      "Francia",
    "France":       "Francia",

    # Italia
    "Italia":       "Italia",
    "ITALIA":       "Italia",
    "italia":       "Italia",

    # México
    "México":       "México",
    "méxico":       "México",
    "Mexico":       "México",
    "mexico":       "México",
    "Mejico":       "México",

    # Perú
    "Perú":         "Perú",
    "Peru":         "Perú",
    "PERU":         "Perú",
    "peru":         "Perú",

    # Portugal
    "Portugal":     "Portugal",
    "PORTUGAL":     "Portugal",
    "portugal":     "Portugal",

    # Reino Unido
    "Reino Unido":      "Reino Unido",
    "reino unido":      "Reino Unido",
    "R. Unido":         "Reino Unido",
    "UK":               "Reino Unido",
    "United Kingdom":   "Reino Unido",

    # República Dominicana
    "Rep. Dominicana":      "República Dominicana",
    "Republica Dominicana": "República Dominicana",
    "R. Dominicana":        "República Dominicana",
    "RD":                   "República Dominicana",

    # Venezuela
    "Venezuela":     "Venezuela",
    "VENEZUELA":     "Venezuela",
    "venezuela":     "Venezuela",
}

def normalizar_paises(valor, diccionario_mapeo):
    valor_limpio = valor.strip()
    if valor_limpio in diccionario_mapeo:

       return (diccionario_mapeo[valor_limpio])

    else:

        print(f"AVISO: valor no reconocido → '{valor}'")

        return valor
    

# ===============================================
# LIMPIAR EMAIL
# ==============================================
def limpiar_email(email):
    if not email:
        return ""

    # Quitar espacios y pasar a minúsculas
    email = email.strip().lower().replace(" ", "")

    # Reemplazar acentos manulmente
    reemplazos_acentos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ñ": "n",
    }

    for viejo, nuevo in reemplazos_acentos.items():
        email = email.replace(viejo, nuevo)

    # Correcciones comunes
    reemplazos = {
        ",": ".",
        ";": ".",
        "..": ".",
        "@@": "@",
        ".@": "@",
    }

    for viejo, nuevo in reemplazos.items():
        email = email.replace(viejo, nuevo)

    # Validación básica
    if (
        "@" in email and
        "." in email.split("@")[-1] and
        email.count("@") == 1
    ):
        return email

    return ""

# ==================================================================
# LIMPIAR TELEFONO
# ============================================================
def limpiar_telefono(telefono):
   

    if not telefono:
        return ""

    telefono = telefono.strip()

    resultado = ""

    for i, c in enumerate(telefono):
        # Mantener + solo al inicio
        if c == "+" and i == 0:
            resultado += c

        # Mantener números
        elif c.isdigit():
            resultado += c

    # Validación mínima
    numeros = resultado.replace("+", "")

    if len(numeros) >= 7:
        return resultado

    return ""
# ================================================================
# PASO A PASO: CÓMO FUNCIONA normalizar_fecha(fecha_texto)
# ================================================================
#
# OBJETIVO: convertir CUALQUIER formato de fecha al estándar DD/MM/AAAA
#
# ESTRATEGIA GENERAL:
#   1. Limpiar el texto (strip)
#   2. Detectar el formato ANTES de intentar convertir
#   3. Extraer día, mes y año por separado
#   4. Formatear siempre como f"{dia:02d}/{mes:02d}/{anio}"
#
# ================================================================


# ── DICCIONARIO DE MESES ────────────────────────────────────────
# Relaciona texto (minúsculas) con su número correspondiente.
# Cubre español (enero, feb, mar...) e inglés (jan, feb, mar...)
# ── ¿Por qué en minúsculas? Porque antes de buscar en el
#    diccionario convertiremos la palabra a minúsculas (.lower()),
#    así "Julio", "JULIO" y "julio" todos funcionarán igual.

meses = {
    "enero":1,      "febrero":2,    "marzo":3,      "abril":4,
    "mayo":5,       "junio":6,      "julio":7,       "agosto":8,
    "septiembre":9, "octubre":10,   "noviembre":11,  "diciembre":12,
    "jan":1,  "feb":2,  "mar":3,  "apr":4,  "may":5,  "jun":6,
    "jul":7,  "aug":8,  "sep":9,  "oct":10, "nov":11, "dec":12,
    # Abreviaturas en español (aparecen en los datos como "28-mar-2026")
    "ene":1,  "abr":4,  "ago":8,  "dic":12
}


# ── CONTADORES GLOBALES ─────────────────────────────────────────
# Los usamos para imprimir el resumen al final.
fechas_normalizadas = 0
fechas_invalidas = 0


# ================================================================
# NORMALIZAR FECHA
# ================================================================

def normalizar_fecha(fecha_texto):
    """
    Recibe una fecha en CUALQUIER formato y devuelve DD/MM/AAAA.
    Si no puede convertirla, devuelve 'FECHA INVÁLIDA'.
    """

    global fechas_normalizadas, fechas_invalidas

    # Paso 1: Limpiar espacios sobrantes
    if not fecha_texto:
        fechas_invalidas += 1
        return "FECHA INVÁLIDA"

    fecha = str(fecha_texto).strip()

    # ────────────────────────────────────────────────────────────
    # DETECTAR FORMATO (el corazón de la función)
    # Usamos if/elif para ir comprobando cada posibilidad.
    # El ORDEN IMPORTA: ponemos los más específicos primero.
    # ────────────────────────────────────────────────────────────

    try:

        # ── FORMATO 1: "DD de mes de AAAA"  →  "15 de julio de 2026"
        # Detectamos: contiene " de "
        if " de " in fecha:
            # split(' de ') separa por ese literal → ["15", "julio", "2026"]
            partes = fecha.split(" de ")
            dia  = int(partes[0])
            mes  = meses[partes[1].lower()]   # convertir texto a número
            anio = int(partes[2])


        # ── FORMATO 2: "mes DD, AAAA"  →  "julio 15, 2026"
        # Detectamos: contiene ',' Y el primer trozo empieza por letra (es texto)
        elif "," in fecha and not fecha[0].isdigit():
            # Quitamos la coma, luego split por espacio → ["julio", "15", "2026"]
            partes = fecha.replace(",", "").split()
            mes  = meses[partes[0].lower()]
            dia  = int(partes[1])
            anio = int(partes[2])


        # ── A partir de aquí todos los formatos tienen separador - o /
        # ── Primero miramos los que usan '-'

        # ── FORMATO 3: "DD-mes-AAAA"  →  "28-mar-2026" o "15-jul-2026"
        # Detectamos: contiene '-' Y la parte del MEDIO es texto (letra)
        elif "-" in fecha and fecha.split("-")[1].isalpha():
            partes = fecha.split("-")           # ["28", "mar", "2026"]
            dia  = int(partes[0])
            mes  = meses[partes[1].lower()]
            anio = int(partes[2])


        # ── FORMATO 4: "AAAA-MM-DD"  →  "2026-07-15"
        # Detectamos: contiene '-' Y el primer trozo tiene 4 dígitos
        elif "-" in fecha and len(fecha.split("-")[0]) == 4:
            partes = fecha.split("-")           # ["2026", "07", "15"]
            anio = int(partes[0])
            mes  = int(partes[1])
            dia  = int(partes[2])


        # ── FORMATO 5: "DD-MM-AAAA"  →  "15-07-2026"
        # Detectamos: contiene '-' Y el primer trozo tiene 1-2 dígitos
        elif "-" in fecha and len(fecha.split("-")[0]) <= 2:
            partes = fecha.split("-")           # ["15", "07", "2026"]
            dia  = int(partes[0])
            mes  = int(partes[1])
            anio = int(partes[2])


        # ── A partir de aquí todos los formatos usan '/'

        # ── FORMATO 6: "DD/M/AA"  →  "15/7/26"  (año de 2 dígitos)
        # Detectamos: contiene '/' Y el último trozo tiene SOLO 2 dígitos
        elif "/" in fecha and len(fecha.split("/")[-1]) == 2:
            partes = fecha.split("/")           # ["15", "7", "26"]
            dia  = int(partes[0])
            mes  = int(partes[1])
            anio = int(partes[2]) + 2000        # 26 → 2026  ← PISTA CLAVE


        # ── FORMATO 7: "DD/MM/AAAA"  →  "15/07/2026"
        # Detectamos: contiene '/' Y el primer trozo tiene 1-2 dígitos
        elif "/" in fecha and len(fecha.split("/")[0]) <= 2:
            partes = fecha.split("/")           # ["15", "07", "2026"]
            dia  = int(partes[0])
            mes  = int(partes[1])
            anio = int(partes[2])


        # ── NINGÚN FORMATO RECONOCIDO
        else:
            print(f"  ⚠  AVISO: formato no reconocido → '{fecha}'")
            fechas_invalidas += 1
            return "FECHA INVÁLIDA"


        # ── FORMATEAR EL RESULTADO ───────────────────────────────
        # :02d garantiza siempre 2 dígitos: 5 → "05", 15 → "15"
        fechas_normalizadas += 1
        return f"{dia:02d}/{mes:02d}/{anio}"


    except (ValueError, KeyError, IndexError) as e:
        # Algo salió mal al convertir (número inválido, mes desconocido...)
        print(f"  ⚠  AVISO: error al parsear '{fecha}' → {e}")
        fechas_invalidas += 1
        return "FECHA INVÁLIDA"
    
# ===========================================================
# ELIMINA FECHA NVALIDA
# =================================================

def procesar_registros(registros):

    registros_limpios = []

    for registro in registros:

        fecha_limpia = normalizar_fecha(
            registro["fecha"]
        )

        # Si la fecha es inválida → eliminar registro
        if fecha_limpia == "FECHA INVÁLIDA":
            continue

        nuevo = {
            "fecha": fecha_limpia,
            "nombre": registro["nombre"]
        }

        registros_limpios.append(nuevo)

    return registros_limpios

# =============== LIMPIAR HORAS =====================
def limpiar_hora(hora):
    """
    Limpia y normaliza una hora.

    Convierte formatos como:
    - "9:5"      -> "09:05"
    - "9.30"     -> "09:30"
    - "0930"     -> "09:30"
    - "9h30"     -> "09:30"
    - " 18:7 "   -> "18:07"

    Devuelve "" si la hora no es válida.
    """

    if not hora:
        return ""

    hora = str(hora).strip().lower()

    # Reemplazos comunes
    hora = hora.replace(".", ":")
    hora = hora.replace("h", ":")

    # Caso 0930 -> 09:30
    if ":" not in hora and hora.isdigit():

        if len(hora) == 4:
            hora = hora[:2] + ":" + hora[2:]

        elif len(hora) == 3:
            hora = "0" + hora[0] + ":" + hora[1:]

    # Validar formato
    if ":" not in hora:
        return ""

    partes = hora.split(":")

    if len(partes) != 2:
        return ""

    hh, mm = partes

    if not hh.isdigit() or not mm.isdigit():
        return ""

    hh = int(hh)
    mm = int(mm)

    # Validar rangos
    if hh < 0 or hh > 23:
        return ""

    if mm < 0 or mm > 59:
        return ""

    return f"{hh:02d}:{mm:02d}"
    


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

# Mapeo de escenarios
mapeo_escenarios = {
    # WiZink Center
    "wizink":                  "WiZink Center",
    "wizink center":           "WiZink Center",
    "wi zink":                 "WiZink Center",
    "palacio de deportes":     "WiZink Center",
    "wizinkcenter":            "WiZink Center",

    # Santiago Bernabéu
    "bernabeu":                "Santiago Bernabéu",
    "santiago bernabeu":       "Santiago Bernabéu",
    "bernabéu":                "Santiago Bernabéu",
    "estadio bernabeu":        "Santiago Bernabéu",

    # Wanda Metropolitano
    "wanda":                   "Wanda Metropolitano",
    "metropolitano":           "Wanda Metropolitano",
    "wanda metropolitano":     "Wanda Metropolitano",
    "civitas metropolitano":   "Wanda Metropolitano",

    # La Riviera
    "riviera":                 "La Riviera",
    "la riviera":              "La Riviera",

    # Sala Apolo
    "apolo":                   "Sala Apolo",
    "sala apolo":              "Sala Apolo",

    # Razzmatazz
    "razz":                    "Razzmatazz",
    "razzmatazz":              "Razzmatazz",

    # Palau Sant Jordi
    "palau":                   "Palau Sant Jordi",
    "palau sant jordi":        "Palau Sant Jordi",

    # IFEMA
    "ifema":                   "IFEMA",
    "ifema madrid":            "IFEMA",

    # Sonar
    "sonar":                   "Sónar",
    "sónar":                   "Sónar",

    "wizink":                  "WiZink Center",
    "wizink center":           "WiZink Center",
    "palacio de deportes":     "WiZink Center",

    "bernabeu":                "Santiago Bernabéu",
    "santiago bernabeu":       "Santiago Bernabéu",

    "wanda":                   "Wanda Metropolitano",
    "metropolitano":           "Wanda Metropolitano",

    "riviera":                 "La Riviera",
    "la riviera":              "La Riviera",

    "apolo":                   "Sala Apolo",
    "sala apolo":              "Sala Apolo",
}


def limpiar_escenario(escenario):
    """
    Limpia el escenario.
    
    Si está vacío devuelve None
    para poder eliminar el registro.
    """

    # Campo vacío
    if escenario is None:
        return None

    escenario = str(escenario).strip().lower()

    # Vacío tras limpiar
    if escenario == "":
        return None

    # Eliminar dobles espacios
    while "  " in escenario:
        escenario = escenario.replace("  ", " ")

    # Quitar acentos manualmente
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
    }

    for viejo, nuevo in reemplazos.items():
        escenario = escenario.replace(viejo, nuevo)

    # Buscar en mapeo
    if escenario in mapeo_escenarios:
        return mapeo_escenarios[escenario]

    return escenario.title()


# ===========================================================
# LIMPIEZA METODOS PAHGO
# ============================================================
mapeo_metodos_pago = {
    # Efectivo
    "efectivo": "Efectivo",
    "EFECTIVO": "Efectivo",
    "Efectivo": "Efectivo",
    "metalico": "Efectivo",
    "Metálico": "Efectivo",
    "Cash": "Efectivo",
    "cash": "Efectivo",
    
    # PayPal
    "paypal": "PayPal",
    "PAYPAL": "PayPal",
    "PayPal": "PayPal",
    "Paypal": "PayPal",
    "Pay Pal": "PayPal",
    "pay pal": "PayPal",
    
    # Tarjeta
    "tarjeta": "Tarjeta",
    "TARJETA": "Tarjeta",
    "Tarjeta": "Tarjeta",
    "tarjeta credito": "Tarjeta",
    "tarjeta de crédito": "Tarjeta",
    "tarjeta de credito": "Tarjeta",
    "Tarjeta de crédito": "Tarjeta",
    "Visa": "Tarjeta",
    "VISA": "Tarjeta",
    
    # Transferencia
    "transferencia": "Transferencia",
    "TRANSFERENCIA": "Transferencia",
    "Transferencia": "Transferencia",
    "transferencia bancaria": "Transferencia",
    "Transfer.": "Transferencia",
    "transfer.": "Transferencia",
    
    # Bizum
    "bizum": "Bizum",
    "BIZUM": "Bizum",
    "Bizum": "Bizum",
    "Bisum": "Bizum",
    "bisum": "Bizum",
    
    # Casos nulos o no especificados
    None: "No especificado",
    "": "No especificado"
}
def limpiar_metodo_pago(metodo_pago):
    """
    Limpia y normaliza el método de pago.
    
    Si está vacío devuelve 'No especificado'
    """

    # Valores nulos
    if metodo_pago is None:
        return "No especificado"

    # Convertir a texto
    metodo_pago = str(metodo_pago).strip()

    # Vacío
    if metodo_pago == "":
        return "No especificado"

    # Pasar a minúsculas
    metodo_pago = metodo_pago.lower()

    # Quitar acentos manualmente
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
    }

    for viejo, nuevo in reemplazos.items():
        metodo_pago = metodo_pago.replace(viejo, nuevo)

    # Eliminar dobles espacios
    while "  " in metodo_pago:
        metodo_pago = metodo_pago.replace("  ", " ")

    # Buscar en mapeo
    if metodo_pago in mapeo_metodos_pago:
        return mapeo_metodos_pago[metodo_pago]

    # Casos especiales
    if "visa" in metodo_pago:
        return "Tarjeta"

    if "mastercard" in metodo_pago:
        return "Tarjeta"

    return metodo_pago


def limpiar_dni(dni):
    """
    Limpia y valida un DNI español.

    Reglas:
    - Elimina espacios y guiones
    - Convierte la letra a mayúscula
    - Valida formato y letra
    - Devuelve "" si no es válido
    """

    if not dni:
        return None

    # Limpiar
    dni = str(dni).strip().upper()

    dni = dni.replace(" ", "")
    dni = dni.replace("-", "")

    # Debe tener 8 números + 1 letra
    if len(dni) != 9:
        return None

    numero = dni[:8]
    letra = dni[8]

    # Validar número
    if not numero.isdigit():
        return None

    # Validar letra
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    letra_correcta = letras[int(numero) % 23]

    if letra != letra_correcta:
        return None

    return numero + letra

# ==========================================
# LIMPIAR mapeo_escenarios
# =================
mapeo_escenarios = {
    # Escenario Principal
    "Esc. Principal":       "Escenario Principal",
    "Escenario Principal":  "Escenario Principal",
    "ESCENARIO PRINCIPAL":  "Escenario Principal",
    "Escenario principal":  "Escenario Principal",
    "escenario principal":  "Escenario Principal",
    "Main Stage":           "Escenario Principal",   # versión en inglés

    # Escenario Bosque
    "Esc. Bosque":          "Escenario Bosque",
    "Escenario Bosque":     "Escenario Bosque",
    "ESCENARIO BOSQUE":     "Escenario Bosque",
    "Escenario bosque":     "Escenario Bosque",
    "escenario bosque":     "Escenario Bosque",

    # Escenario Luna
    "Esc. Luna":            "Escenario Luna",
    "Escenario Luna":       "Escenario Luna",
    "ESCENARIO LUNA":       "Escenario Luna",
    "Escenario luna":       "Escenario Luna",
    "escenario luna":       "Escenario Luna",

    # Escenario Sol
    "Esc. Sol":             "Escenario Sol",
    "Escenario Sol":        "Escenario Sol",
    "ESCENARIO SOL":        "Escenario Sol",
    "Escenario sol":        "Escenario Sol",
    "escenario sol":        "Escenario Sol",

    # Escenario Río
    "Esc. Río":             "Escenario Río",
    "Esc. Rio":             "Escenario Río",   # falta tilde
    "Escenario Río":        "Escenario Río",
    "Escenario Rio":        "Escenario Río",   # falta tilde
    "ESCENARIO RIO":        "Escenario Río",   # falta tilde
    "escenario rio":        "Escenario Río",   # falta tilde
}


def limpiar_escenario(escenario):
    
    # Campo vacío
    if escenario is None:
        return None

    escenario = str(escenario).strip()

    if escenario == "":
        return None

    # Normalizar
    escenario = escenario.lower()

    # Quitar acentos manualmente
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
    }

    for viejo, nuevo in reemplazos.items():
        escenario = escenario.replace(viejo, nuevo)

    # Eliminar dobles espacios
    while "  " in escenario:
        escenario = escenario.replace("  ", " ")

    # Mapeo normalizado
    mapeo_normalizado = {}

    for clave, valor in mapeo_escenarios.items():

        clave_normalizada = clave.lower()

        for viejo, nuevo in reemplazos.items():
            clave_normalizada = clave_normalizada.replace(viejo, nuevo)

        mapeo_normalizado[clave_normalizada] = valor

    # Buscar en el mapeo
    if escenario in mapeo_normalizado:
        return mapeo_normalizado[escenario]

    # Si no existe
    return escenario.title()


# ================================================================
# LIMPIAR EMAIL
# =================================================

def limpiar_email(email):
    """
    Comprueba si un email es válido.

    Reglas básicas:
    - Debe tener un solo @
    - Debe tener dominio
    - Debe tener punto después del @
    - No puede tener espacios
    """

    if not email:
        return "Email no válido"

    email = str(email).strip()

    # No espacios
    if " " in email:
        return "Email no válido"

    # Debe tener un solo @
    if email.count("@") != 1:
        return "Email no válido"

    usuario, dominio = email.split("@")

    # Usuario vacío
    if usuario == "":
        return "Email no válido"

    # Dominio vacío
    if dominio == "":
        return "Email no válido"

    # Debe existir un punto en dominio
    if "." not in dominio:
        return "Email no válido"

    # El punto no puede estar al inicio o final
    if dominio.startswith(".") or dominio.endswith("."):
        return "Email no válido"

    return (email)
# ======================================================
# LIMPIAR TELEFONO
# ===============================================
def limpiar_telefono(telefono):
    """
    Limpia y normaliza teléfonos españoles.

    Reglas:
    - Elimina espacios
    - Elimina guiones
    - Elimina paréntesis
    - Convierte 0034XXXXXXXXX → +34XXXXXXXXX
    - Mantiene formato final: +34XXXXXXXXX
    - Si no es válido → "Teléfono no válido"
    """

    if telefono is None:
        return "Teléfono no válido"

    telefono = str(telefono).strip()

    if telefono == "":
        return "Teléfono no válido"

    # Eliminar caracteres innecesarios
    caracteres_eliminar = [
        " ",
        "-",
        "(",
        ")",
        "."
    ]

    for c in caracteres_eliminar:
        telefono = telefono.replace(c, "")

    # 0034XXXXXXXXX → +34XXXXXXXXX
    if telefono.startswith("0034"):
        telefono = "+" + telefono[2:]

    # Si empieza por 34 sin +
    elif telefono.startswith("34") and len(telefono) == 11:
        telefono = "+" + telefono

    # Si tiene 9 dígitos españoles
    elif telefono.isdigit() and len(telefono) == 9:
        telefono = "+34" + telefono

    # Validar formato final
    if not telefono.startswith("+34"):
        return "Teléfono no válido"

    numeros = telefono[3:]

    # Deben ser 9 números
    if not numeros.isdigit():
        return "Teléfono no válido"

    if len(numeros) != 9:
        return "Teléfono no válido"

    # Debe empezar por 6, 7, 8 o 9
    if numeros[0] not in ["6", "7", "8", "9"]:
        return "Teléfono no válido"

    return telefono

# ==============================================
# LIMPIAR CATEGORIA
# ========================
mapeo_categorias = {
    # Oro (nivel alto)
    "Oro":     "Oro",
    "ORO":     "Oro",
    "oro":     "Oro",
    "Oro ":    "Oro",     # espacio final
    "Gold":    "Oro",     # inglés
    "GOLD":    "Oro",     # inglés

    # Plata (nivel medio)
    "Plata":   "Plata",
    "PLATA":   "Plata",
    "Silver":  "Plata",   # inglés
    "SILVER":  "Plata",   # inglés

    # Bronce (nivel bajo)
    "Bronce":  "Bronce",
    "BRONCE":  "Bronce",
    "bronce":  "Bronce",
    "Bronze":  "Bronce",  # inglés
    "BRONZE":  "Bronce",  # inglés
}

def limpiar_categoria(categoria):
    """
    Limpia y normaliza la categoría.

    Categorías válidas:
    - Oro
    - Plata
    - Bronce

    Si no es válida:
    → "Categoría no válida"
    """

    if categoria is None:
        return "Categoría no válida"

    categoria = str(categoria).strip()

    if categoria == "":
        return "Categoría no válida"

    # Pasar a minúsculas
    categoria = categoria.lower()

    # Eliminar dobles espacios
    while "  " in categoria:
        categoria = categoria.replace("  ", " ")

    # Crear mapeo normalizado
    mapeo_normalizado = {}

    for clave, valor in mapeo_categorias.items():

        clave_normalizada = clave.strip().lower()

        mapeo_normalizado[clave_normalizada] = valor

    # Buscar categoría
    if categoria in mapeo_normalizado:
        return mapeo_normalizado[categoria]

    return "Categoría no válida"


# ========================================================
# LIMPIAR TIPOS ENTRADA
# ========================================================


mapeo_tipos_entrada = {
    # General
    "General":   "General",
    "GENERAL":   "General",
    "general":   "General",
    "general ":  "General",   # espacio final
    "Gral":      "General",   # abreviatura
    "Gral.":     "General",   # abreviatura con punto

    # Premium
    "Premium":   "Premium",
    "premium":   "Premium",
    "PREMIUM":   "Premium",
    "Prémium":   "Premium",   # tilde incorrecta (no lleva)
    "Premiun":   "Premium",   # typo (n por m al final)

    # VIP
    "VIP":       "VIP",
    "Vip":       "VIP",
    "vip":       "VIP",
    "VIP ":      "VIP",       # espacio final
    " VIP":      "VIP",       # espacio inicial
    "V.I.P.":    "VIP",       # con puntos
}

def limpiar_tipo_entrada(tipo_entrada):
    """
    Limpia y normaliza el tipo de entrada.

    Tipos válidos:
    - General
    - Premium
    - VIP

    Si no es válido:
    → "Tipo de entrada no válido"
    """

    if tipo_entrada is None:
        return "Tipo de entrada no válido"

    tipo_entrada = str(tipo_entrada).strip()

    if tipo_entrada == "":
        return "Tipo de entrada no válido"

    # Pasar a minúsculas
    tipo_entrada = tipo_entrada.lower()

    # Quitar acentos manualmente
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
    }

    for viejo, nuevo in reemplazos.items():
        tipo_entrada = tipo_entrada.replace(viejo, nuevo)

    # Eliminar dobles espacios
    while "  " in tipo_entrada:
        tipo_entrada = tipo_entrada.replace("  ", " ")

    # Crear mapeo normalizado
    mapeo_normalizado = {}

    for clave, valor in mapeo_tipos_entrada.items():

        clave_normalizada = clave.strip().lower()

        for viejo, nuevo in reemplazos.items():
            clave_normalizada = clave_normalizada.replace(viejo, nuevo)

        mapeo_normalizado[clave_normalizada] = valor

    # Buscar en el mapeo
    if tipo_entrada in mapeo_normalizado:
        return mapeo_normalizado[tipo_entrada]

    return "Tipo de entrada no válido"

# ================================================================
# PROCESAR 
# ================================================================


# id_artista,nombre,genero_musical,pais,cache_eur,email_manager,telefono
def procesar_artistas(lista):
#     ## recorrer la lista y a cada item
#      # limpiezaitem['nombre]
    lista_limpia=[]
    for item in lista:
        item_limpio= {
            "id_artista": item['id_artista'],
            "nombre": normalizar_texto(item['nombre']),
            "genero_musical": normalizar_categoria(item['genero_musical'], mapeo_generos   ),
            "pais": normalizar_paises(item['pais'], mapeo_paises),
            "cache_eur": limpiar_valor_numerico(item['cache_eur']),
            "email_manager":limpiar_email(item['email_manager']),
            "telefono": limpiar_telefono(item['telefono'])
        }
        if item_limpio["telefono"] != "Teléfono no válido":
            lista_limpia.append(item_limpio)
        if item_limpio["email_manager"] != "Email no válido":
            lista_limpia.append(item_limpio)
        
    return lista_limpia

def procesar_escenarios(lista):
    lista_limpia=[]
    for item in lista:
        item_limpio= {
            "fecha": normalizar_fecha(item['fecha']),
            "escenario": limpiar_escenario(item['escenario']),
            "artista": normalizar_texto(item['artista']),
            "hora_inicio": limpiar_hora(item['hora_inicio']),
            "hora_fin": limpiar_hora(item['hora_fin']),
            "soundcheck": limpiar_hora(item['soundcheck']),
            "notas": normalizar_texto(item['notas'])
        }
        if item_limpio["fecha"] != "FECHA INVÁLIDA":
            lista_limpia.append(item_limpio)
    return lista_limpia

def procesar_patrocinadores(lista):
    lista_limpia=[]
    for item in lista:
        item_limpio= {
            "nombre_empresa": normalizar_texto(item['nombre_empresa']),
            "contacto": normalizar_texto(item['contacto']),
            "email": limpiar_email(item['email']),
            "importe_patrocinio": limpiar_valor_numerico(item['importe_patrocinio']),
            "categoria": limpiar_categoria(item['categoria']),
            "fecha_inicio": normalizar_fecha(item['fecha_inicio']),
            "fecha_fin": normalizar_fecha(item['fecha_fin'])
        }
        if item_limpio["email"] != "Email no válido":
            lista_limpia.append(item_limpio)
        if item_limpio["contacto"] != "Sin Datos":
            lista_limpia.append(item_limpio)
    return lista_limpia

def procesar_entradas(lista):
    lista_limpia=[]
    for item in lista:
        item_limpio= {
            "id_venta": item['id_venta'],
            "nombre_comprador": normalizar_texto(item['nombre_comprador']),
            "email": limpiar_email(item['email']),
            "dni": limpiar_dni(item['dni']),
            "tipo_entrada": limpiar_tipo_entrada(item['tipo_entrada']),
            "precio": limpiar_valor_numerico(item['precio']),
            "fecha_compra": normalizar_fecha(item['fecha_compra']),
            "metodo_pago": limpiar_metodo_pago(item['metodo_pago'])

        }
        lista_limpia.append(item_limpio)
    return (lista_limpia)