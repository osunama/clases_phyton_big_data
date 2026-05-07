
try:
    numero = int(input('Dime un numero: '))
    numero2 = int(input('Dime otro numero: '))
    resultado = numero / numero2
    print(resultado)
except ValueError:
    print('Los valores introducidos no son numeros')
except ZeroDivisionError:
    print('no se puede dividir por cero')
    #por si hay un error no previsto
except:
    print('futuro error no previsto')


print('otros calculos')