
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


if __name__ == "__main__":
    print(twist_sequence([1, 2, 3, 4, 5], 2))
    # [4, 5, 1, 2, 3]
