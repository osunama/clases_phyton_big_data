# para leer un excel hay que instalar la libreria openpyxl escribiendo en el terminal: pip install openpyxl
from openpyxl import load_workbook

#cargar el fichero de excel en nuestro archivo
excel = load_workbook('./data/empleados.xlsx')
# seleccionar la hoja que quiero. Hoja activa.
hoja = excel.active

# recorrer filas y columnas de la hoja de excel
for fila in hoja.iter_rows()