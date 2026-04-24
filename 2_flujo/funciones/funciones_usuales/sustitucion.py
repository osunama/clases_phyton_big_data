#quitar acentos
otra_frase = "Él envió más café frío allá después según él también pidió algún té allí recién así él podría reír todavía."

# otra_frase = otra_frase.lower()
# otra_frase = otra_frase.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")

# print(otra_frase)

#resuelto por Juanan dentro de una función para poder ser reutilizada

def quitar_acentos(texto):
    return texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
resultado = quitar_acentos(otra_frase)
print (resultado)


nombre = "   Juan Antonio   "
print(f'Hola')