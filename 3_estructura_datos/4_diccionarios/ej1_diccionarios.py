producto = {
"title": "Televisión 4K 55 pulgadas",
"price": 899,
"quantity": 2,
"tax": 21
}

producto1 = {
"title": "Sillón masaje",
"price": 455,
"quantity": 4,
"tax": 10
}
#esto es un carrito de compra. Extraer el PVP. precio* cantidad -tax
def PVP():
    base = producto["price"] * producto["quantity"]
    iva = base * producto["tax"] / 100
    total = base + iva
    return total

print(PVP())


#RESULTO POR jUANAN
#PVP = (Precio * cantidad) + (Precio * cantidad) * 0,21
# def calcular_pvp(producto_dict):
#     pvp = (producto_dict['price'] * producto_dict['quantity']) + ((producto_dict['price'] * producto_dict['quantity']) * producto_dict["tax"]/ 100)
#     print(pvp)
    
# calcular_pvp(producto)
# calcular_pvp(producto1)
