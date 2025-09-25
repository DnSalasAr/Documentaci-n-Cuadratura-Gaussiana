"""
Gaussian Quadrature integration for the function x^6 - sin(2x)*x^2 from 1 to 3.

This script finds the optimal number of sample points N for accurate integration.
"""

from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np

def gaussxw(N):
    """
    Calculate Gaussian quadrature points and weights for interval [-1, 1].
    
    Args:
        N (int): Number of sample points
        
    Returns:
        tuple: (x, w) where x are the sample points and w are the weights
        
    Example:
        >>> x, w = gaussxw(3)
        >>> print(f"Points: {x}, Weights: {w}")
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """
    Scale Gaussian quadrature from [-1, 1] to arbitrary interval [a, b].
    
    Args:
        a (float): Lower limit of integration
        b (float): Upper limit of integration
        x (array): Sample points in [-1, 1]
        w (array): Weights in [-1, 1]
        
    Returns:
        tuple: (x_scaled, w_scaled) scaled to [a, b]
        
    Example:
        >>> x, w = gaussxw(3)
        >>> x_scaled, w_scaled = gaussxwab(0, 2, x, w)
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


muestreo7, peso7 = gaussxw(7)
muestreo7, peso7 = gaussxwab(1, 3, muestreo7, peso7)

def polinomio(varInd):
    """
    Function to integrate: x^6 - sin(2x)*x^2
    
    Args:
        varInd (float or array): Input value(s)
        
    Returns:
        float or array: Function value(s)
    """
    return varInd**6 -  np.sin(2*varInd)* varInd**2 


difMinima = float('inf')
masCerca = 0
mejorN = 0  

for i in range(1,15):
    muestreo, peso = gaussxw(i)
    muestreo, peso = gaussxwab(1, 3, muestreo, peso)
    Integral = np.sum(polinomio(muestreo) * peso)
    
    print(f"Valor de la integral con N={i}: {Integral}")
    
    if abs(Integral - 317.344246673826356) < difMinima:
        difMinima = abs(Integral - 317.344246673826356)
        masCerca = Integral
        mejorN = i

print(f"\nEl mas cercano al valor esperado es: {masCerca}, con N={mejorN}")