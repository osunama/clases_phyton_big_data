## try - except 
# try maneja la parte correcta o parte esperada
# except maneja el posible error.

try:
    entrada = input('Dime un numero: ')
    numero = int(entrada)
    print(numero)
except ValueError:
    print(f'has introducido un valor no numerico: {entrada}')
    
print('cosas')