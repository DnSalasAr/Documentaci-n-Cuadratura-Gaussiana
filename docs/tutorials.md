# Tutorial

## Uso básico

```python

from cuadrature import gaussxw, gaussxwab, polinomio

# Integrar la función de 1 a 3 con 7 puntos
N = 7

from cuadrature import calcular_integral, encontrar_N_optimo

# Calcular la integral con un número específico de puntos
N = 7
resultado = calcular_integral(N)
print(f"Resultado con N={N}: {resultado}")

# Encontrar el N óptimo automáticamente por convergencia
N_optimo, valor_optimo, historia = encontrar_N_optimo(tolerancia=1e-10)

print(f"\nN óptimo encontrado: {N_optimo}")
print(f"Valor de la integral: {valor_optimo}")
print(f"Diferencia con valor de referencia: {abs(valor_optimo - 317.344246673826356)}")

```

