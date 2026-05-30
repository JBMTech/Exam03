
def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    """
    Escribe una función que convierta un número de una base a otra.
    Admite bases de 2 a 36 inclusive, usando dígitos 0-9 y letras A-Z para
    los valores 10-35. Devuelve "ERROR" si la entrada no es válida
    (base, dígitos).
    """
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Verificar bases válidas
    if from_base < 2 or from_base > 36:
        return "ERROR"
    if to_base < 2 or to_base > 36:
        return "ERROR"
    
    number = number.upper()

    # ---------- Convertir de base origen a decimal ----------
    decimal_value = 0

    for char in number:
        if char not in digits:
            return "ERROR"
        
        value = digits.index(char)

        if value >= from_base:
            return "ERROR"
        
        decimal_value = decimal_value * from_base + value
    
    if decimal_value == 0:
        return "0"
    
    # ---------- Convertir de decimal a base destino ----------
    result = ""

    while decimal_value > 0:
        remainder = decimal_value % to_base
        result = digits[remainder] + result
        decimal_value = decimal_value // to_base
    
    return result
