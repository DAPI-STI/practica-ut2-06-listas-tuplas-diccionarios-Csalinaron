"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float] = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}
from collections import defaultdict

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    """
    Recibe un carrito como lista de tuplas (producto, unidades).

    Devuelve:
    - Un diccionario con el coste por producto (producto -> coste)
    - Un float con el total general

    Reglas:
    - Si units < 0 -> ValueError
    - Si un producto no existe en PRICES -> ValueError
    - Si un producto aparece varias veces, se acumulan unidades

    Ejemplo:
    [("Pan", 2), ("Huevos", 1), ("Pan", 1)] ->
      ({"Pan": 4.2, "Huevos": 2.3}, 6.5)
    """
    if not cart:
        return ({}, 0.0)
    
    units_by_product = defaultdict(int)
    
    for product, units in cart:
        if units < 0:
            raise ValueError(f"Unidades negativas: {product}")
        if product not in PRICES:
            raise ValueError(f"Producto no existe: {product}")
        units_by_product[product] += units
    
    cost_by_product = {}
    total = 0.0
    
    for product, total_units in units_by_product.items():
        cost = round(PRICES[product] * total_units, 2)
        cost_by_product[product] = cost
        total += cost
    
    total = round(total, 2)
    
    return (cost_by_product, total)
    
    

    raise NotImplementedError("Implementa checkout(cart)")
