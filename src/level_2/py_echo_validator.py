
def echo_validator(text: str) -> bool:
    """
    Escribe una función que compruebe si una cadena es un
    palíndromo, ignorando espacios y mayúsculas/minúsculas,
    y considerando solo caracteres alfabéticos en la comparación.
    """
    if text.replace(" ", "").isalpha():
        cleaned = text.replace(" ", "").lower()
        if cleaned == cleaned[::-1]:
            return True
        return False
    return False
