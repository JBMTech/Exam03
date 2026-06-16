
def hidenp(small: str, big: str) -> bool:
    """
    Escribe una función que compruebe si la cadena «small» es una
    subsecuencia de «big». Una subsecuencia significa que todos
    los caracteres de «small» aparecen en «big» en el mismo orden,
    aunque no necesariamente de forma consecutiva.
    La función distingue entre mayúsculas y minúsculas.
    """
    i = 0

    for c in big:
        if i < len(small) and c == small[i]:
            i += 1
    
    return i == len(small)
