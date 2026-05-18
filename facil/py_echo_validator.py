
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


# Entrada
# echo_validator("racecar")
# Salida
# True
# Entrada
# echo_validator("A man a plan a canal Panama")
# Salida
# True
# Entrada
# echo_validator("race a car")
# Salida
# False
# Entrada
# echo_validator("Was it a car or a cat I saw")
# Salida
# True
# Entrada
# echo_validator("hello")
# Salida
# False
# Entrada
# echo_validator("Madam Im Adam")
# Salida
# True
# Entrada
# echo_validator("")
# Salida
# False
