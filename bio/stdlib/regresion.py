# stdlib/regresion.py

def regresion_lineal(xs, ys):
    """
    xs, ys: listas de números (mismo tamaño).
    Devuelve un diccionario modelo con pendiente m y bias b.
    """
    if len(xs) != len(ys) or len(xs) == 0:
        raise Exception("regresion_lineal: listas vacías o de distinto tamaño")

    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))

    denom = (n * sxx - sx * sx)
    if denom == 0:
        raise Exception("regresion_lineal: datos degenerados")

    m = (n * sxy - sx * sy) / denom
    b = (sy - m * sx) / n
    
    promedio_y = sy / n
    ss_tot = sum((y - promedio_y) ** 2 for y in ys)
    ss_res = sum((y - (m * x + b)) ** 2 for x, y in zip(xs, ys))
    r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
    
    return {"m": m, "b": b, "r2": r2}

def predecir(modelo, x):
    """
    modelo: dict con 'm' y 'b'
    x: número o lista de números.
    """
    m = modelo["m"]
    b = modelo["b"]
    if isinstance(x, (list, tuple)):
        return [m * xi + b for xi in x]
    else:
        return m * x + b

