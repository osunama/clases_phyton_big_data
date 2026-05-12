import csv
import os

RUTA_CSV = os.path.join(os.path.dirname(__file__), "data", "game.csv")


def cargar_juegos(ruta=RUTA_CSV):
    """Carga el CSV y devuelve una lista de diccionarios."""
    juegos = []
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            fila["id"]       = int(fila["id"])
            fila["precio"]   = float(fila["precio"])
            fila["en_stock"] = fila["en_stock"].strip() == "1"
            juegos.append(fila)
    return juegos


def mostrar_en_stock(juegos):
    """1 - Muestra los juegos que están en stock."""
    en_stock = [j for j in juegos if j["en_stock"]]

    print("\n🎮 JUEGOS EN STOCK")
    print("-" * 52)
    print(f"  {'Título':<28} {'Género':<12} {'Precio':>7}")
    print("-" * 52)
    for j in en_stock:
        print(f"  {j['titulo']:<28} {j['genero']:<12} {j['precio']:>6.2f} €")
    print(f"\n  Total: {len(en_stock)} juego(s) en stock de {len(juegos)}")
    return en_stock


def crear_rebajas(juegos, descuento=0.20, ruta_salida=None):
    """2 - Crea rebajas.csv con todos los juegos rebajados un 20%."""
    if ruta_salida is None:
        ruta_salida = os.path.join(os.path.dirname(RUTA_CSV), "rebajas.csv")

    rebajados = []
    for j in juegos:
        copia = j.copy()
        copia["precio_original"] = round(j["precio"], 2)
        copia["precio"]          = round(j["precio"] * (1 - descuento), 2)
        rebajados.append(copia)

    campos = ["id", "titulo", "genero", "precio_original", "precio", "lanzamiento", "en_stock"]
    with open(ruta_salida, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(rebajados)

    print(f"\n💸 REBAJAS ({int(descuento * 100)}% de descuento)")
    print("-" * 52)
    print(f"  {'Título':<28} {'Original':>9} {'Rebajado':>9}")
    print("-" * 52)
    for j in rebajados:
        print(f"  {j['titulo']:<28} {j['precio_original']:>8.2f} € {j['precio']:>8.2f} €")
    print(f"\n  Archivo guardado en: {ruta_salida}")
    return rebajados


def juego_mas_caro_y_barato(juegos):
    """3 - Devuelve e imprime el juego más caro y más barato."""
    if not juegos:
        print("No hay juegos disponibles.")
        return None, None

    mas_caro   = max(juegos, key=lambda j: j["precio"])
    mas_barato = min(juegos, key=lambda j: j["precio"])

    print("\n💰 PRECIO MÁS CARO Y MÁS BARATO")
    print("-" * 52)
    print(f"  Más caro:   {mas_caro['titulo']:<30} {mas_caro['precio']:>6.2f} €")
    print(f"  Más barato: {mas_barato['titulo']:<30} {mas_barato['precio']:>6.2f} €")
    return mas_caro, mas_barato
