"""
Cálculo de integral definida usando cuadratura gaussiana.
Integrando (x^6 - sin(2x)·x^6. 
La integral es de 1 a 3.

Este programa encuentra el número óptimo de puntos N mediante convergencia sucesiva (sugerecia del profesor) y calcula la integral.
"""
from scipy.special import legendre
import numpy as np

def gaussxw(N):
    """
    Calcula los puntos y pesos de cuadratura gaussiana para el intervalo [-1, 1], usando los ppolinomios de Legendre
    
    Args:
        N (int): Número de puntos de muestreo
        
    Returns:
        tuple: (x, w) donde x son los puntos y w son los pesos
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """
    Escala la cuadratura gaussiana del intervalo [-1, 1] a [a, b].
    
    Args:
        a (float): Límite inferior de integración
        b (float): Límite superior de integración
        x (array): Puntos de muestreo en [-1, 1]
        w (array): Pesos en [-1, 1]
        
    Returns:
        tuple: (x_escalado, w_escalado) en el intervalo [a, b]
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def integrando(x):
    """
    Función a integrar: f(x) = x^6 - sin(2x)·x^2
    
    Args:
        x (float): Puntos donde se evalua la función

    Returns:
        float: Imagen de la función
    """
    
    return x**6 - np.sin(2*x) * x**2

def calcular_integral(N, a=1, b=3): #En este caso la integral es de 1 a 3, por eso a y b tienen valores predeterminados
    """
    Calcula la integral usando cuadratura gaussiana con N puntos.
    
    Args:
        N (int): Número de puntos de muestreo
        a (float): Límite inferior (default: 1)
        b (float): Límite superior (default: 3)
        
    Returns:
        float: Valor aproximado de la integral
    """
    x, w = gaussxw(N)
    x_esc, w_esc = gaussxwab(a, b, x, w)
    return np.sum(integrando(x_esc) * w_esc)

def encontrar_N_optimo(tolerancia=1e-10, N_max=20):
    """
    Encuentra el N óptimo comparando I_N+1 con I_N hasta que sean iguales (diferencia muy pequeña entre ellos).
    
    Args:
        tolerancia (float): Diferencia mínima para considerar convergencia
        N_max (int): Número máximo de iteraciones
        
    Returns:
        tuple: (N_optimo, valor_integral, historia_convergencia)
    """
    
    # Inicializar variables
    I_anterior = calcular_integral(1)  # Empezar con N=1
    historial = []  # Para guardar la historia de convergencia
    
    print(f"N=1: I = {I_anterior:.10f}")
    
    for N in range(2, N_max + 1):
        I_actual = calcular_integral(N)
        diferencia = abs(I_actual - I_anterior)
        
        historial.append((N, I_actual, diferencia))
        print(f"N={N}: I = {I_actual:.10f}, |I_N - I_N-1| = {diferencia:.2e}")
        
        # Verificar convergencia
        if diferencia < tolerancia:
            print(f"I_{N} ≈ I_{N-1} con diferencia: {diferencia:.2e}")
            return N, I_actual, historial
        
        I_anterior = I_actual
    
    print(f"\nNo se alcanzó convergencia en {N_max} iteraciones")
    print(f"Última diferencia: {historial[-1][2]:.2e}")
    return N_max, I_actual, historial

if __name__ == "__main__":
    # Ejecutar la búsqueda de convergencia
    N_optimo, valor_optimo, historial = encontrar_N_optimo()
        
    print(f"RESULTADO FINAL:")
    print(f"N óptimo: {N_optimo}")
    print(f"Valor de la integral: {valor_optimo:.13f}")#El último decimal pueder variar por el error de redondeo y de punto flotante. 
                                                        #Pero justo puso esos decimales en el .md, entonces así se va. Sería mejor poner menos en ambas siempre
    print(f"Diferencia con WolframAlpha: {abs(valor_optimo - 317.344246673826356):.2e}")
