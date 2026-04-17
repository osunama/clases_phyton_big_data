nota = float(input('Dime tu nota'))

if nota >= 0 and nota < 5:
    print('Suspenso')
  
if nota >= 5 and nota <= 10:
    print('Aprobado')

if nota > 10:
    print('No valida')
    
# """"""
#  Pide por input el importe de una compra
# Si el importe es mayor que 100 muestra el mensaje:
# "Aplicamos un 10% de descuento"
#  Y además, mostramos el precio con el descuento aplicado
# """"""

importe = float(input('Importe: '))
if importe > 100:
    print('10% de descuento')
    importe_total = importe * 0.9
    print(f'Precio original: {importe}€. Precio con decuento: {importe_total}€')