
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    """
    Escribe una función que fusione dos listas ordenadas en una sola
    lista ordenada.
    """
    list1.extend(list2)
    list1.sort()
    return list1
