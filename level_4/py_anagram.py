
def anagram(s1: str, s2: str) -> bool:
    """
    Escribe una función que compruebe si dos cadenas son anagramas.
    Deben contener exactamente las mismas letras en la misma cantidad,
    sin tener en cuenta las mayúsculas ni los espacios.
    """
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)