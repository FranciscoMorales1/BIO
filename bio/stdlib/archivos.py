# stdlib/archivos.py

def cargar(ruta):
    """
    Lee un archivo de texto y devuelve una lista de líneas (sin saltos de línea).
    El usuario del lenguaje puede parsear las líneas como necesite.
    """
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = f.read().splitlines()
    return lineas

def guardar(ruta, datos):
    """
    Escribe datos en un archivo de texto.
    - Si datos es lista, escribe una línea por elemento.
    - Si es otro tipo, escribe str(datos).
    """
    with open(ruta, "w", encoding="utf-8") as f:
        if isinstance(datos, (list, tuple)):
            for linea in datos:
                f.write(str(linea) + "\n")
        else:
            f.write(str(datos))
