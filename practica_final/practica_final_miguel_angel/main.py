from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml

from lib.limpieza import  normalizar_texto, limpiar_valor_numerico, normalizar_categoria, mapeo_generos, normalizar_paises, mapeo_paises, limpiar_email, limpiar_telefono, normalizar_fecha, limpiar_hora, limpiar_escenario
from lib.exportacion import crear_csv, crear_excel

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
            "genero_musical": normalizar_categoria(item['genero_musical'], mapeo_generos   ),
            "pais": normalizar_paises(item['pais'], mapeo_paises),
            "cache_eur": limpiar_valor_numerico(item['cache_eur']),
            "email_manager":limpiar_email(item['email_manager']),
            "telefono": limpiar_telefono(item['telefono'])
        }
        lista_limpia.append(item_limpio)
    return lista_limpia

artistas_limpio = procesar_artistas(artistas)
# creacion del fichero en base a los datos limpias
crear_csv(artistas_limpio, 'artistas_limpio.csv', 'datos_limpios')


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
        lista_limpia.append(item_limpio)
    return lista_limpia

escenarios_horarios_limpio = procesar_escenarios(escenarios_horarios)
crear_csv(escenarios_horarios_limpio, 'escenarios_horario_limpio.csv', 'datos_limpios')

def procesar_patrocinadores(lista):
    lista_limpia=[]
    for item in lista:
        item_limpio= {
            "nombre_empresa": normalizar_texto(item['nombre_empresa']),
            "contacto": normalizar_texto(item['contacto']),
            "email": limpiar_email(item['email']),
            "importe_patrocinio": limpiar_valor_numerico(item['importe_patrocinio']),
            "categoria": normalizar_texto(item['categoria']),
            "fecha_inicio": normalizar_fecha(item['fecha_inicio']),
            "fecha_fin": normalizar_fecha(item['fecha_fin'])
        }
        lista_limpia.append(item_limpio)
    return lista_limpia

patrocinadores_limpio = procesar_patrocinadores(patrocinadores)
crear_csv(patrocinadores_limpio, "patrocinadotres_limpio.csv", 'datos_limpios')


def procesar_entradas(lista):
    lista_limpia=[]
    for item in lista:
        item_limpio= {
            "id_venta": item['id_venta'],
            "nombre_comprador": normalizar_texto(item['nombre_comprador']),
            "email": limpiar_email(item['email']),
            "dni": normalizar_texto(item['dni']),
            "tipo_entrada": normalizar_texto(item['tipo_entrada']),
            "precio": limpiar_valor_numerico(item['precio']),
            "fecha_compra": normalizar_texto(item['fecha_compra']),
            "metodo_pago": normalizar_texto(item['metodo_pago'])

        }
        lista_limpia.append(item_limpio)
    return (lista_limpia)

venta_entradas_limpio = procesar_entradas(ventas_entradas)
crear_csv(venta_entradas_limpio, "venta_entradas_limpio.csv", 'datos_limpios')

datos_excel = {
    "artistas": artistas_limpio,
    "escenarios": escenarios_horarios_limpio,
    "patrocinadores": patrocinadores_limpio,
    "ventas": venta_entradas_limpio
}

crear_excel(
    'festival_musica.xlsx',
    'datos_limpios',
    datos_excel
)


