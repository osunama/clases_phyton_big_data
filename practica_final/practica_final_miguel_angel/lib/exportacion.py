import csv
from openpyxl import Workbook


def crear_csv(lista, nombre, carpeta):
    fichero = open(f"./{carpeta}/{nombre}", 'w', encoding='UTF-8', newline='')
    # saber las cabeceras.
    cabeceras = []
    for key in lista[0].keys():
        cabeceras.append(key)
    #volcar los datos de la lista en un objeto csv
    mi_csv = csv.DictWriter(fichero, fieldnames=cabeceras) 
    #imprimir cabeceras en la primera linea
    mi_csv.writeheader()
    # Escribir cada fila en el csv
    mi_csv.writerows(lista)
    # cerramos el ficher
    fichero.close()

def crear_excel(nombre_archivo, carpeta, hojas):
   
    # Crear libro
    wb = Workbook()

    # Eliminar hoja inicial vacía
    wb.remove(wb.active)

    # Crear una hoja por dataset
    for nombre_hoja, datos in hojas.items():

        # Crear hoja
        hoja = wb.create_sheet(title=nombre_hoja)

        # Evitar errores si la lista está vacía
        if not datos:
            continue

        # Cabeceras
        cabeceras = list(datos[0].keys())
        hoja.append(cabeceras)

        # Filas
        for item in datos:
            fila = [item[campo] for campo in cabeceras]
            hoja.append(fila)

    # Guardar archivo
    wb.save(f'./{carpeta}/{nombre_archivo}')



