
def bracket_validator(s: str) -> bool:
    """Escribe una función que compruebe si los paréntesis de una cadena
    están bien emparejados y anidados.
    Admite tres tipos: (), [], {}.

    La función debe:
    - Devolver True si todos los paréntesis están bien emparejados
    - Devolver True si la cadena no tiene paréntesis
    - Devolver False si faltan pares o el anidamiento es incorrecto
    - Ignorar caracteres que no sean paréntesis
    """
    result = " "

    s.replace("()", " ").replace("[]", " ").replace("{}", " ")
    if s == result:
        return True
    else:
        return False


if __name__ == "__main__":
    print(bracket_validator("()"))


# Entrada
# bracket_validator("()")
# Salida
# True
# Entrada
# bracket_validator("()[]{}")
# Salida
# True
# Entrada
# bracket_validator("(]")
# Salida
# False
# Entrada
# bracket_validator("([)]")
# Salida
# False
# Entrada
# bracket_validator("{[]}")
# Salida
# True
# Entrada
# bracket_validator("hello(world)[test]{code}")
# Salida
# True
# Entrada
# bracket_validator("((()))")
# Salida
# True
# Entrada
# bracket_validator("((())")
# Salida
# False
# Entrada
# bracket_validator("")
# Salida
# True