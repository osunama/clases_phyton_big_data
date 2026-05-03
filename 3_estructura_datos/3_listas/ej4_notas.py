# =============================================================================
# EJERCICIO 4: NOTAS DE CLASE — INSERTAR, ORDENAR Y ESTADÍSTICAS
# Tienes una lista de notas de un examen.
# Añade tres notas más con append() y una en la posición 2 con insert().
# Muestra la lista ordenada de mayor a menor.
# Calcula y muestra la media, la nota más alta y la más baja.
# Cuenta cuántos alumnos han aprobado (nota >= 5).
# notas = [7.5, 4.0, 8.5, 6.0, 9.0, 3.5, 5.5]
# =============================================================================

# menu, pintar el menu con las opciones - lista notas, añadir una nota al final, añadir una nota por posicion, mostrar la lista ordenada, calcular media, calcular maximo, calcular minimo, cuantos alumnos han aprobado. salir
notas = [7.5, 4.0, 8.5, 6.0, 9.0, 3.5, 5.5]
def mostrar_ordenadas():
    ordenadas = sorted(notas, reverse=True)
    for i, nota in enumerate(ordenadas, 1):
        return ordenadas
def contar_aprobados():
    aprobados = len([n for n in notas if n >= 5])
    return aprobados
def calcular_media():
    media = sum(notas) / len(notas)
    return media
    
def mostrar_notas(notas):
    for nota in notas:
        if nota < 5:
            print( f'\033[31m {nota} \033[0m' )
        else:
            print( f'\033[32m {nota} \033[0m' ) # verde
def inserta_nota(nota, posicion=len(notas)):
    notas.insert(posicion, nota)

def main():
    menu = """## Bienvenido a la aplicación de notas ##
    [1]. Listar la notas
    [2]. Añadir nueva nota
    [3]. Añadir nueva nota en cualquier posición
    [4]. Ordenar por mayor a menor
    [5]. Calcular media
    [6]. Calcular máximo
    [7]. Calcular mínimo
    [8]. Numero de alumnos aprobados
    [x]. Salir
    """
    print(menu)
    option = input('Dime que opcion quieres: ')
    print('-' * 40)
    if option == '1':
        mostrar_notas(notas)
    elif option == '2':
        input('Añadir nota:')
    elif option == '3':
        print('Añadir nota por posición')
    elif option == '4':
        print(mostrar_ordenadas())
    elif option == '5':
        print(calcular_media())
    elif option == '6':
        print(f'Nota más alta: {max(notas)}')
    elif option == '7':
        print(f'Nota más baja: {min(notas)}')
    elif option == '8':
        print(contar_aprobados())
    elif option == 'x':
        print('Hasta pronto')
        return
    else:
        print('Opcion no valida')
    print('-' * 40)
    print(' ')
    main()
    


main()
