#La base del codigo no difiere con la referencia del lab 4
from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np

def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)
    
    return x, w

def gaussxwab(a, b, x, w):
    # Obtenido de pag 168 Newman)

    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

muestreo7, peso7 = gaussxw(7)
muestreo7, peso7 = gaussxwab(1, 3, muestreo7, peso7)
def polinomio(varInd):
    return varInd**6 -  np.sin(2*varInd)* varInd**2 
#Se esperaria que el resultado mas exacto fuera con N=7, pero la mejor forma de hacerlo es probando con distintos valores de N
#Con WolframAlpha se obtiene que la integral definida de 1 a 3 de x^6 - sen(2x)*x^2 es 317.344246673826356...
difMinima = float('inf')
masCerca = 0
mejorN = 0  

#Esta parte se podria mejorar y empezar en N=5, porque se esperaria que los primeros den valores mas lejanos. 
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
#Curiosamente no dio N=7, dio N=9, por eso lo mejor era probar y no solo decir
