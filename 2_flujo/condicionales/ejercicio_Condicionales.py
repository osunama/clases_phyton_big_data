numero_horas = float(input('¿Cuántas horas has estado en el parking?'))
tarjeta_residente = input('¿Eres residente [s/n]?').lower()
tipo_vehiculo = input('¿Que vehículo tienes?[moto/coche/furgoneta]').lower()

if numero_horas <= 0:
    print("Error: Las horas deben ser mayores que 0")
# elif tarjeta_residente != "s" and tarjeta_residente != "n": de esta otra manera se comprueban todo a la vez
elif tarjeta_residente not in ("s","n"):
    print("Error: Debes introducir 's' o 'n'")

elif tipo_vehiculo not in ("moto","coche","furgoneta"):
    print("Vehiculo incorrecto")
# si todo correcto, hacemos el calculo en el else

else:
    if numero_horas <=1:
        precio = 2
    elif numero_horas <=3:
        precio = 2 + (numero_horas - 1)*1.5
    else:
        precio = 2 + (2 * 1.5) + (numero_horas -3)
    if tipo_vehiculo == "moto":
        precio = precio*0.7
    if tipo_vehiculo == "coche":
        precio = precio*1
    if tipo_vehiculo == "furgoneta":
        precio = precio*1.5
    if tarjeta_residente == "s":
        precio = precio * 0.80
    print(f'Has estado {numero_horas}. Precio: {precio}€.')

"""
    - Multiplicador de precio dependiendo del vehículo:
        moto x 0.7, coche x 1, furgoneta x 1.5

    - Aplica 20% descuento sobre el precio si erees residente

    FORMATO:
    --- TICKET DE APARCAMIENTO ---
    Horas: 2.5 | Vehículo: coche | Residente: sí
    Precio base: 3.75 €
    Descuento residente: -0.75 €
    TOTAL: 3.00 €
"""