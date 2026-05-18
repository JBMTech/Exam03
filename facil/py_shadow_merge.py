
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    """
    Escribe una función que fusione dos listas ordenadas en una sola
    lista ordenada.
    """
    list1.extend(list2)
    list1.sort()
    return list1


if __name__ == "__main__":

    print(f"Salida: {shadow_merge([1, 3, 5], [2, 4, 6])}")
    print(f"Salida: {shadow_merge([1, 2, 3], [4, 5, 6])}")
    print(f"Salida: {shadow_merge([1], [2, 3, 4])}")
    print(f"Salida: {shadow_merge([], [1, 2, 3])}")
    print(f"Salida: {shadow_merge([1, 1, 2], [1, 3, 3])}")
