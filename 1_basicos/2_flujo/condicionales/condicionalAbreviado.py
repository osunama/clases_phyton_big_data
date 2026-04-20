# Usar para definir el valor de una variable en función de una condición

estado_luz = False
if estado_luz:
    mensaje = "La luz esta encendida"
else:
    mensaje = "Luz apagada"
# igual que lo de arriba pero sol en un mensaje
mensaje = "Luz encendida" if estado_luz else "Luz Apagada"
print(mensaje)
