
def echo_validator(text: str) -> bool:
    """
    Escribe una función que compruebe si una cadena es un
    palíndromo, ignorando espacios y mayúsculas/minúsculas,
    y considerando solo caracteres alfabéticos en la comparación.
    """
    if text.isalpha():
        result: list = text.replace(" ", "").lower()
        if result == result[::-1]:
            return True
        return False
    return False


if __name__ == "__main__":
    print(echo_validator("racecar"))
