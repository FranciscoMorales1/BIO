# stdlib/matematicas.py

import math
import random 

def potencia(x, y):
    return x ** y

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

def aleatorio():
    return random.random()

def aleatorio_entero(a, b):
    return random.randint(a, b)

def aleatorio_rango(a, b):
    return random.uniform(a, b)
