from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml

from lib.limpieza import procesar_artistas, procesar_entradas, procesar_escenarios, procesar_patrocinadores
from lib.exportacion import crear_csv, crear_excel

artistas = cargar_csv('datos', 'artistas.csv') 

escenarios_horarios = cargar_excel('datos', 'escenarios_horarios.xlsx')

ventas_entradas = cargar_json('datos', 'ventas_entradas.json')

patrocinadores = cargar_xml('datos', 'patrocinadores.xml')


artistas_limpio = procesar_artistas(artistas)
# creacion del fichero en base a los datos limpias
crear_csv(artistas_limpio, 'artistas_limpio.csv', 'datos_limpios')



escenarios_horarios_limpio = procesar_escenarios(escenarios_horarios)
crear_csv(escenarios_horarios_limpio, 'escenarios_horario_limpio.csv', 'datos_limpios')



patrocinadores_limpio = procesar_patrocinadores(patrocinadores)
crear_csv(patrocinadores_limpio, "patrocinadotres_limpio.csv", 'datos_limpios')



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

