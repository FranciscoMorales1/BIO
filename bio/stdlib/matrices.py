# stdlib/matrices.py

# Utilidades internas

def es_matriz(m):
    return isinstance(m, list) and (len(m) == 0 or isinstance(m[0], list))

def es_matriz_uniforme(m):
    if not es_matriz(m):
        return False
    if len(m) == 0:
        return True
    ancho = len(m[0])
    return all(isinstance(fila, list) and len(fila) == ancho for fila in m)

def mismas_dimensiones(a, b):
    if not (es_matriz(a) and es_matriz(b)):
        return False
    if len(a) != len(b):
        return False
    return all(len(a[i]) == len(b[i]) for i in range(len(a)))

def operar_elemento_a_elemento(a, b, op):
    filas = len(a)
    cols = len(a[0]) if filas > 0 else 0
    return [
        [op(a[i][j], b[i][j]) for j in range(cols)]
        for i in range(filas)
    ]

# =====================
# Operaciones públicas
# =====================

def sumar_matrices(a, b):
    """Suma elemento a elemento."""
    if not mismas_dimensiones(a, b):
        raise Exception("sumar_matrices: dimensiones incompatibles")
    return operar_elemento_a_elemento(a, b, lambda x, y: x + y)

def restar_matrices(a, b):
    """Resta elemento a elemento."""
    if not mismas_dimensiones(a, b):
        raise Exception("restar_matrices: dimensiones incompatibles")
    return operar_elemento_a_elemento(a, b, lambda x, y: x - y)

def mmult(a, b):
    """Multiplicación matricial clásica (matriz A x matriz B)."""
    if not (es_matriz_uniforme(a) and es_matriz_uniforme(b)):
        raise Exception("mmult: matrices irregulares")
    if len(a) > 0 and len(a[0]) != len(b):
        raise Exception("mmult: dimensiones incompatibles")

    filas = len(a)
    cols = len(b[0]) if len(b) > 0 else 0
    inter = len(b)

    resultado = []
    for i in range(filas):
        fila = []
        for j in range(cols):
            acum = 0
            for k in range(inter):
                acum += a[i][k] * b[k][j]
            fila.append(acum)
        resultado.append(fila)
    return resultado

def transpuesta(m):
    """Transpuesta de una matriz."""
    if not es_matriz_uniforme(m):
        raise Exception("transpuesta: matriz irregular")
    if len(m) == 0:
        return []
    return [list(fila) for fila in zip(*m)]

def inversa(m):
    """Inversa de una matriz cuadrada usando Gauss-Jordan."""
    if not es_matriz_uniforme(m):
        raise Exception("inversa: matriz irregular")
    n = len(m)
    if n == 0:
        return []
    if n != len(m[0]):
        raise Exception("inversa: solo matrices cuadradas")

    # Copia profunda
    a = [fila[:] for fila in m]
    identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Matriz aumentada [A | I]
    for i in range(n):
        a[i] += identidad[i]

    # Gauss-Jordan
    for i in range(n):
        pivote = a[i][i]
        if pivote == 0:
            raise Exception("inversa: matriz no invertible (pivote 0)")
        # Normalizar fila
        for j in range(2 * n):
            a[i][j] /= pivote
        # Eliminar en otras filas
        for k in range(n):
            if k != i:
                factor = a[k][i]
                for j in range(2 * n):
                    a[k][j] -= factor * a[i][j]

    # Extraer parte derecha como inversa
    inv = [fila[n:] for fila in a]
    return inv

def ceros_vector(tamano):
    return [0 for _ in range(tamano)]

def ceros_matriz(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]

def dimensiones(estructura):
    dims = []
    actual = estructura
    while isinstance(actual, list):
        dims.append(len(actual))
        if len(actual) == 0:
            break
        actual = actual[0]
    return tuple(dims)
