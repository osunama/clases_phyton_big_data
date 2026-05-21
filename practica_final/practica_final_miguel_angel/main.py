from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml

from lib.limpieza import limpiar_texto, normalizar_texto

artistas = cargar_csv('datos', 'artistas.csv') 

cargar_excel('datos', 'escenarios_horarios.xlsx')

cargar_json('datos', 'ventas_entradas.json')

cargar_xml('datos', 'patrocinadores.xml')


print(limpiar_texto("     jkh     jhnng    "))

print(normalizar_texto("    jose jose jóse"))



# def procesar(lista):
#     ## recorrer la lista y a cada item
#          # 
#          # limpiezaitem['nombre]
#     for item in lista:
#         item


