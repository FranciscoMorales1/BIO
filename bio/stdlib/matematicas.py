# stdlib/matematicas.py

import math

def potencia(x, y):
    return x ** y

# raiz cuadrada → raiz(x)
# raiz n-esima → raiz(x, n)
def raiz(x, n=2):
    return x ** (1.0 / n)

def sen(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def asin(x):
    return math.asin(x)

def acos(x):
    return math.acos(x)

def atan(x):
    return math.atan(x)
