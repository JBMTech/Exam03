def count_vowels(word: str) -> int:
    vowels = "aeiou"
    count = 0

    for i in word.lower():
        if i in vowels:
            count += 1
    return count


def cryptic_sorter(strings: list[str]) -> list[str]:
    """
    Escribe una función que ordene una lista de cadenas con prioridad
    en tres niveles:
    1. Primario: por longitud (ascendente)
    2. Secundario: lexicográfico (alfabético, sin distinguir mayúsculas,
    ascendente)
    3. Terciario: por número de vocales (ascendente si la longitud y el orden
    léxico coinciden)

    La función debe manejar:
    - Cadenas vacías y listas vacías
    - Mayúsculas y minúsculas mezcladas (tratar como minúsculas al ordenar)
    - Caracteres especiales (ignorarlos al contar vocales)
    """
    result = strings.copy()

    for i in range(len(result)):
        for j in range(len(result) - 1 - i):

            a = result[j]
            b = result[j + 1]

            # ¿Debe "a" ir después de "b"?
            should_swap = False

            if len(a) > len(b):
                should_swap = True

            elif len(a) == len(b):

                if a.lower() > b.lower():
                    should_swap = True

                elif a.lower() == b.lower():
                    if count_vowels(a) > count_vowels(b):
                        should_swap = True

            if should_swap:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result
