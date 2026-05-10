# Crea un script en Python que pida al usuario su número de ticket de compra y, tras validar que la entrada no contenga letras (mostrando un error si las hay) calcule el premio correspondiente

# ["Un Café Gratis", "10% de Descuento" , "Un Bolígrafo"]

# premio se obtiene resto el numero ticket entre 5. El dato obtenido es la posicion de la lista

# si el numero se sale rango no hay premio

premios = ["Un Café Gratis", "10% de Descuento", "Un Bolígrafo"]

ticket = input("Introduce tu número de ticket: ")

if not ticket.isdigit():
    print("Error: el ticket no puede contener letras.")
else:
    posicion = int(ticket) % 5
    if posicion < len(premios):
        print(f"¡Felicidades! Tu premio es: {premios[posicion]}")
    else:
        print("Lo sentimos, este ticket no tiene premio.")