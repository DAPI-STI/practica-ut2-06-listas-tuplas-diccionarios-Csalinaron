"""
EX01 (Listas)
Invertir una lista sin modificar la original.
"""

def reverse_list(values: list[int]) -> list[int]:
    """
    Devuelve una NUEVA lista con los elementos de `values` en orden inverso.

    - No modifiques la lista original.

    Ejemplos:
    - reverse_list([1, 2, 3]) -> [3, 2, 1]
    - reverse_list([]) -> []
    """
    l1 = values [::-1]
    return l1

    raise NotImplementedError("Implementa reverse_list(values)")
