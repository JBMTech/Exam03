
def pattern_tracker(text: str) -> int:
    """
    Escribe una función que cuente cuántos pares consecutivos
    de dígitos válidos hay en una cadena. Un par válido son dos
    dígitos adyacentes donde el segundo es exactamente uno mayor
    que el primero. Un 9 seguido de 0 NO es un par válido.
    """
    count = 0
    i = 0

    while i < len(text) - 1:

        # Verificar ambos sean digitos
        if text[i].isdigit() and text[i + 1].isdigit():

            first = int(text[i])
            second = int(text[i + 1])

            # Verificar si el segundo es exactamente +1
            if second == first + 1:
                count += 1
        i += 1
    return count


if __name__ == "__main__":
    print(pattern_tracker("112233"))
