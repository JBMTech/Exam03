
def string_permutation_checker(s1: str, s2: str) -> bool:
    """
    Escribe una función que determine si dos cadenas son permutaciones
    entre sí.
    Dos cadenas son permutaciones si contienen los mismos caracteres con
    las mismas frecuencias.

    La función debe:
    - Comprobar que ambas cadenas tienen exactamente los mismos caracteres
    - Contar frecuencias (distingue mayúsculas y minúsculas)
    - Devolver True si son permutaciones, False en caso contrario
    - Manejar cadenas vacías (dos vacías son permutación)
    - Tratar espacios y puntuación como caracteres normales
    """
    # return sorted(s1) == sorted(s2)
    if len(s1) != len(s2):
        return False

    count = {}

    # count s1
    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # restar con s2
    for char in s2:
        if char in count:
            count[char] -= 1
        else:
            return False

    # verificar todo en 0:
    for value in count.values():
        if value != 0:
            return False

    return True
