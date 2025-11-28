# stdlib/graficas.py

import matplotlib.pyplot as plt

def graficar(x, y, titulo=None, xlabel="x", ylabel="y"):
    """
    x, y: listas de números del mismo tamaño.
    """
    if len(x) != len(y):
        raise Exception("graficar: x e y deben tener el mismo tamaño")

    plt.figure()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if titulo is not None:
        plt.title(titulo)
    plt.grid(True)
    plt.show()
