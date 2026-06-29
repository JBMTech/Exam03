
def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Escribe una función que espeje una matriz 2D horizontalmente
    invirtiendo cada fila.

    La función debe:
    - Recibir una lista 2D (matriz) de enteros
    - Devolver una nueva lista 2D donde cada fila esté invertida
    horizontalmente
    - Manejar matrices de cualquier tamaño (cuadradas o rectangulares)
    - Conservar el orden original de las filas
    - No modificar la matriz original
    """
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix
