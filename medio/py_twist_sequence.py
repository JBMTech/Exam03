
def twist_sequence(arr: list[int], k: int) -> list[int]:
    """
    Escribe una función que rote un arreglo hacia la derecha k posiciones;
    rotar a la derecha k posiciones significa que los últimos k elementos se
    mueven al frente.
    """

    # Verificar lista vacia
    if len(arr) == 0:
        return []

    # Evitar vueltas innecesarias
    k = k % len(arr)

    # Dividir y reorganizar
    return arr[-k:] + arr[:-k]
