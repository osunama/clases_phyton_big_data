from functions import (
    cargar_juegos,
    mostrar_en_stock,
    crear_rebajas,
    juego_mas_caro_y_barato,
)

# Cargar datos desde game.csv
juegos = cargar_juegos()

# 1 - Juegos en stock
mostrar_en_stock(juegos)

# 2 - Crear rebajas.csv con 20% de descuento
crear_rebajas(juegos, descuento=0.20)

# 3 - Juego más caro y más barato
juego_mas_caro_y_barato(juegos)
