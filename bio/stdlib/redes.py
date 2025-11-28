# stdlib/redes.py

import random
import math

# ---------- Utilidades ----------

def _sigmoide(x):
    return 1.0 / (1.0 + math.exp(-x))

def _dsigmoide(y):
    # y = sigmoide(x), derivada respecto a x
    return y * (1.0 - y)

# ---------- MLP ----------

def crear_red(estructura):
    """
    estructura: lista de enteros, p.ej [2, 4, 1]
    Devuelve un diccionario 'red' con pesos y biases.
    """
    if len(estructura) < 2:
        raise Exception("crear_red: se necesitan al menos capa de entrada y salida")

    pesos = []
    biases = []
    for i in range(len(estructura) - 1):
        entradas = estructura[i]
        salidas = estructura[i + 1]
        # matriz salidas x entradas
        capa_pesos = [[random.uniform(-1, 1) for _ in range(entradas)] for _ in range(salidas)]
        capa_biases = [0.0 for _ in range(salidas)]
        pesos.append(capa_pesos)
        biases.append(capa_biases)

    return {
        "estructura": estructura,
        "pesos": pesos,
        "biases": biases
    }

def _forward(red, x):
    """Propagación hacia adelante. x es lista de números."""
    activaciones = x[:]
    activaciones_por_capa = [activaciones]

    for capa_pesos, capa_biases in zip(red["pesos"], red["biases"]):
        nueva = []
        for j in range(len(capa_pesos)):
            suma = sum(w * a for w, a in zip(capa_pesos[j], activaciones)) + capa_biases[j]
            nueva.append(_sigmoide(suma))
        activaciones = nueva
        activaciones_por_capa.append(activaciones)

    return activaciones_por_capa

def entrenar(red, X, Y, epocas, tasa=0.1):
    """
    X: lista de vectores de entrada
    Y: lista de vectores de salida esperada (one-hot o valores entre 0 y 1)
    """
    if len(X) != len(Y):
        raise Exception("entrenar: X y Y deben tener el mismo número de ejemplos")

    for _ in range(epocas):
        for x, y_esperado in zip(X, Y):
            # FORWARD
            activaciones_por_capa = _forward(red, x)
            salidas = activaciones_por_capa[-1]

            # BACKPROP
            # error en capa de salida
            deltas = []
            delta_salida = [
                (salidas[j] - y_esperado[j]) * _dsigmoide(salidas[j])
                for j in range(len(salidas))
            ]
            deltas.append(delta_salida)

            # capas ocultas hacia atrás
            for i in range(len(red["pesos"]) - 2, -1, -1):
                capa_pesos_siguiente = red["pesos"][i + 1]
                delta_siguiente = deltas[0]
                activ_capa = activaciones_por_capa[i + 1]
                delta_actual = []
                for j in range(len(activ_capa)):
                    error = sum(
                        capa_pesos_siguiente[k][j] * delta_siguiente[k]
                        for k in range(len(delta_siguiente))
                    )
                    delta_actual.append(error * _dsigmoide(activ_capa[j]))
                deltas.insert(0, delta_actual)

            # actualizar pesos y biases
            for i in range(len(red["pesos"])):
                activ_entrada = activaciones_por_capa[i]
                delta_capa = deltas[i]
                for j in range(len(red["pesos"][i])):  # neurona en capa i+1
                    for k in range(len(activ_entrada)):  # neurona en capa i
                        red["pesos"][i][j][k] -= tasa * delta_capa[j] * activ_entrada[k]
                    red["biases"][i][j] -= tasa * delta_capa[j]

def clasificar(red, x):
    """Devuelve el índice de la neurona con mayor activación en la salida."""
    activaciones_por_capa = _forward(red, x)
    salida = activaciones_por_capa[-1]
    max_val = max(salida)
    return salida.index(max_val), salida

# ---------- K-means para AGRUPAR ----------

def agrupar(datos, k, epocas=100):
    """
    K-means simple.
    datos: lista de vectores numéricos.
    k: número de grupos.
    Devuelve (centroides, asignaciones)
    """
    if len(datos) == 0:
        raise Exception("agrupar: no hay datos")
    dim = len(datos[0])
    # inicializar centroides aleatorios desde los datos
    centroides = random.sample(datos, k)

    for _ in range(epocas):
        # asignación
        grupos = [[] for _ in range(k)]
        for punto in datos:
            distancias = [
                sum((p - c) ** 2 for p, c in zip(punto, centroide))
                for centroide in centroides
            ]
            idx = distancias.index(min(distancias))
            grupos[idx].append(punto)

        # actualizar centroides
        nuevos_centroides = []
        for grupo, centroide in zip(grupos, centroides):
            if len(grupo) == 0:
                nuevos_centroides.append(centroide)
            else:
                nuevo = [
                    sum(p[i] for p in grupo) / len(grupo)
                    for i in range(dim)
                ]
                nuevos_centroides.append(nuevo)
        centroides = nuevos_centroides

    # asignación final
    asignaciones = []
    for punto in datos:
        distancias = [sum((p - c) ** 2 for p, c in zip(punto, centroide)) for centroide in centroides]
        idx = distancias.index(min(distancias))
        asignaciones.append(idx)

    return centroides, asignaciones
