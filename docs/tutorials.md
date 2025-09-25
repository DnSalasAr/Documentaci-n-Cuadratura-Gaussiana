# Tutorial

## Uso básico

```python
from cuadrature import gaussxw, gaussxwab, polinomio

# Integrate the function from 1 to 3 with 7 points
N = 7
x, w = gaussxw(N)
x_scaled, w_scaled = gaussxwab(1, 3, x, w)
result = sum(polinomio(x_scaled) * w_scaled)

print(f"Integration result with N={N}: {result}")

# Test different numbers of points to find optimal N
difMinima = float('inf')
masCerca = 0
mejorN = 0

for i in range(1, 15):
    x, w = gaussxw(i)
    x_scaled, w_scaled = gaussxwab(1, 3, x, w)
    Integral = sum(polinomio(x_scaled) * w_scaled)

    print(f"N={i}: {Integral}")

    # Con WolframAlpha se sabe que el valor de la integral es el siguiente
    expected = 317.344246673826356
    if abs(Integral - expected) < difMinima:
        difMinima = abs(Integral - expected)
        masCerca = Integral
        mejorN = i

print(f"Optimal N: {mejorN}, Value: {masCerca}, Difference: {difMinima}") 
```

