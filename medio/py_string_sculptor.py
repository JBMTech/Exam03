
def string_sculptor(text: str) -> str:
    """
    Escribe una función que transforme una cadena alternando
    mayúsculas y minúsculas solo en caracteres alfabéticos.
    Los demás permanecen igual y no cuentan para la alternancia.
    El primer carácter alfabético debe ser minúscula, el segundo
    mayúscula, el tercero minúscula, y así sucesivamente.
    """
    result = ""
    count = 0
    for i in range(len(text)):
        if text[i].isalpha():
            if count % 2 == 0:
                result += text[i].lower()
            else:
                result += text[i].upper()
            count += 1
        else:
            result += text[i]
        
    return result
