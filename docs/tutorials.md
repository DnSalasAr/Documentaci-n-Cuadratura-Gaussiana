# Tutorial

## Uso básico

```python

from cuadrature import gaussxw, gaussxwab, polinomio, calcular_integral, encontrar_N_optimo

# Integrar la función de 1 a 3 con 7 puntos
N = 7

# Calcular la integral con un número específico de puntos (el rango predeterminado es de 1 a 3)
N = 7
resultado = calcular_integral(N)
print(f"Resultado con N={N}: {resultado}")

# Encontrar el N óptimo automáticamente por convergencia
N_optimo, valor_optimo, historia = encontrar_N_optimo(tolerancia=1e-10)

print(f"\nN óptimo encontrado: {N_optimo}")
print(f"Valor de la integral: {valor_optimo}")
print(f"Diferencia con valor de referencia: {abs(valor_optimo - 317.344246673826356)}")

```
## Uso con diferentes funciones e intervalos
```python
# Definir una nueva función para integrar
def mi_funcion(x):
    return np.exp(-x**2) * np.sin(x)

# Integrar la nueva función de 0 a 2
def integrar_funcion_personalizada(func, a, b, N):
    """
    Integra cualquier función usando cuadratura gaussiana
    """
    x, w = gaussxw(N)
    x_esc, w_esc = gaussxwab(a, b, x, w)
    return np.sum(func(x_esc) * w_esc)

# Ejemplo de uso
resultado_personalizado = integrar_funcion_personalizada(mi_funcion, 0, 2, 10)
print(f"Integral de e^(-x²)sin(x) de 0 a 2: {resultado_personalizado}")
```

