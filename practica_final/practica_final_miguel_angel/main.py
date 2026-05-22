from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml

from lib.limpieza import limpiar_texto, normalizar_texto, limpiar_valor_numerico, eliminar_vacios, normalizar_categoria

artistas = cargar_csv('datos', 'artistas.csv') 

escenarios_horarios = cargar_excel('datos', 'escenarios_horarios.xlsx')

ventas_entradas = cargar_json('datos', 'ventas_entradas.json')

patrocinadores = cargar_xml('datos', 'patrocinadores.xml')


# print(limpiar_texto("     jkh     jhnng    "))

# print(normalizar_texto("    jose jose jóse"))

# print(limpiar_valor_numerico("150.000$"))

# eliminar_vacios()




# id_artista,nombre,genero_musical,pais,cache_eur,email_manager,telefono
def procesar_artistas(lista):
#     ## recorrer la lista y a cada item
#      # limpiezaitem['nombre]
    lista_limpia=[]
    for item in lista:
        item_limpio= {
            "id_artista": item['id_artista'],
            "nombre": normalizar_texto(item['nombre']),
            "genero_musical": normalizar_texto(item['genero_musical']),
            "pais": normalizar_texto(item['pais']),
            "cache_eur": normalizar_texto(item['cache_eur']),
            "email_manager": normalizar_texto(item['email_manager']),
            "telefono": normalizar_texto(item['telefono'])
        }
        lista_limpia.append(item_limpio)
    return lista_limpia

artistas_limpio = procesar_artistas(artistas)

def procesar_escenarios(lista):
    lista_limpia=[]
    for item in lista:
        item_limpio= {
            "fecha": item['fecha'],
            "escenario": normalizar_texto(item['escenario']),
            "artista": normalizar_texto(item['artista']),
            "hora_inicio": normalizar_texto(item['hora_inicio']),
            "hora_fin": normalizar_texto(item['hora_fin']),
            "soundcheck": normalizar_texto(item['soundcheck']),
            "notas": normalizar_texto(item['notas'])
        }
        lista_limpia.append(item_limpio)
    return lista_limpia

escenarios_horarios_limpio = procesar_escenarios(escenarios_horarios)

def procesar_patrocinadores(lista):
    lista_limpia=[]
    for item in lista:
        item_limpio= {
            "nombre_empresa": item['nombre_empresa'],
            "contacto": normalizar_texto(item['contacto']),
            "email": normalizar_texto(item['email']),
            "importe_patrocinio": normalizar_texto(item['importe_patrocinio']),
            "categoria": normalizar_texto(item['categoria']),
            "fecha_inicio": normalizar_texto(item['fecha_inicio']),
            "fecha_fin": normalizar_texto(item['fecha_fin'])
        }
        lista_limpia.append(item_limpio)
    return lista_limpia

patrocinadores_limpio = procesar_patrocinadores(patrocinadores)

def procesar_entradas(lista):
    lista_limpia=[]
    for item in lista:
        item_limpio= {
            "id_venta": item['id_venta'],
            "nombre_comprador": normalizar_texto(item['nombre_comprador']),
            "email": normalizar_texto(item['email']),
            "dni": normalizar_texto(item['dni']),
            "tipo_entrada": normalizar_texto(item['tipo_entrada']),
            "precio": normalizar_texto(item['precio']),
            "fecha_compra": normalizar_texto(item['fecha_compra']),
            "metodo_pago": normalizar_texto(item['metodo_pago'])

        }
        lista_limpia.append(item_limpio)
    return (lista_limpia)

venta_entradas_limpio = procesar_entradas(ventas_entradas)
