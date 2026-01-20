"""
EX04 (Tuplas)
Trabajar con una lista de tuplas (nombre, nota) y devolver una tupla.
"""

def best_student(records: list[tuple[str, float]]) -> tuple[str, float]:
    """
    Recibe una lista de tuplas (nombre, nota) y devuelve la tupla del alumno con mayor nota.

    - Si records está vacío, lanza ValueError.
    - Si hay empate, devuelve el primero que aparezca con esa nota.

    Ejemplo:
    [("Ana", 7.5), ("Luis", 9.0), ("Marta", 8.0)] -> ("Luis", 9.0)
    """
   
    if not records:
        raise ValueError("La lista de registros está vacía")
    
    # Inicializar con el primer estudiante
    best_name, best_score = records[0]
    
    # Recorrer el resto de registros
    for name, score in records[1:]:
        # Comparar solo la nota (índice 1 de la tupla)
        if score > best_score:
            best_name, best_score = name, score
    
    return (best_name, best_score)

    raise NotImplementedError("Implementa best_student(records)")
