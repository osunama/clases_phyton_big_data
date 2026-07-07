def clasificar_nivel(puntos):
    if puntos < 100:
        return "Novato"
    elif puntos <= 499:
        return "Aprendiz"
    elif puntos <= 999:
        return "Veterano"
    else:
        return "Maestro"
print(clasificar_nivel(50))
print(clasificar_nivel(250))
print(clasificar_nivel(750))
print(clasificar_nivel(1500))

# --------------------------------------

def sumar_lista(numeros):
    total = 0

    for numero in numeros:
        total += numero

    return total

lista = [10, 25, 8, 42, 15]
resultado = sumar_lista(lista)

print(resultado)

# --------------------------
def filtrar_pares(numeros):
    return [n for n in numeros if n % 2 == 0]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_pares(lista)

print(resultado)


# -------------------------------
producto = {
    'nombre': 'TV',
    'precio': 49.99,
    'stock': 3
}

for clave, valor in producto.items():
    print(clave, valor)

producto['precio'] = 99.99

producto['categoria'] = 'electrónica'

print(producto)

# -------------- 8 -----------------

tienda ={
    "nombre": "TechStore",
    "productos":[
        {"id":1,"nombre":"Teclado","precio":45.0},
        {"id":1,"nombre":"Ratón","precio":25.0},
        {"id":1,"nombre":"Monitor","precio":299.0}
    ]
}

print (tienda)

tienda ={
    "nombre": "TechStore",
    "productos":[
        {"id":1,"nombre":"Teclado","precio":45.0},
        {"id":2,"nombre":"Ratón","precio":25.0},
        {"id":3,"nombre":"Monitor","precio":299.0}
    ]
}

print (tienda)
total = 0
for producto in tienda["productos"]:
    print("Nombre:", producto["nombre"])
    print("Precio:", producto["precio"])
    total += producto["precio"]

print("Precio total:", total)

# --------------- 9 ------------

ventas =[
    {"producto":"Teclado", "cantidad": 5, "precio":45.0},
    {"producto":"Ratón", "cantidad": 12, "precio":25.0},
    {"producto":"Monitor", "cantidad": 2, "precio":299.0},
    {"producto":"Auriculares", "cantidad": 8, "precio":60.0},
]

ordenada = sorted(ventas, key=lambda x: x['cantidad'], reverse=True)

print(ordenada)


for producto in ordenada:
    total = producto['cantidad'] * producto['precio']
    print(total)


# ----------------- 10 -------

clientes_enero = [1, 2, 3, 4, 5, 2, 3]
clientes_febrero = [3, 4, 5, 6, 7, 4, 5]

set_enero = set(clientes_enero)
set_febrero = set(clientes_febrero)

print("Compraron en ambos meses:", set_enero & set_febrero)
print("Solo en enero:", set_enero - set_febrero)
print("Clientes únicos totales:", set_enero | set_febrero)


