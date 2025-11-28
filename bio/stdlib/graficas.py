# stdlib/graficas.py

import matplotlib.pyplot as plt

# ... (mantener la función graficar original) ...

def graficar_regresion(x, y, m, b):
    """
    Grafica puntos de datos + línea de regresión en UNA sola gráfica.
    
    Parámetros:
    - x: lista de valores x (datos originales)
    - y: lista de valores y (datos originales)
    - m: pendiente de la regresión
    - b: intersección de la regresión
    """
    if len(x) != len(y):
        raise Exception("graficar_regresion: x e y deben tener el mismo tamaño")
    
    plt.figure(figsize=(10, 6))
    
    # Graficar puntos originales (scatter)
    plt.scatter(x, y, color='blue', s=15, alpha=0.15, label='Datos', zorder=2)
    
    # Calcular línea de regresión
    x_min = min(x)
    x_max = max(x)
    x_linea = [x_min, x_max]
    y_linea = [m * x_min + b, m * x_max + b]
    
    # Graficar línea
    plt.plot(x_linea, y_linea, color='red', linewidth=2, 
             label=f'y = {m:.3f}x + {b:.3f}', zorder=1)
    
    # Configuración
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    plt.title('Regresión Lineal', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.show()
