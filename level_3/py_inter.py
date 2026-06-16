
def inter(s1: str, s2: str) -> str:
    """
    Escribe una función que devuelva una cadena con los caracteres que aparecen
    en ambas cadenas, sin repeticiones. Los caracteres se añaden en el orden
    en que aparecen en la primera cadena.
    """
    result = ""

    for c in s1:
        if c in s2 and c not in result:
            result += c
    return result

