# Tutorial

## Basic Usage

```python
from cuadrature import integrate_function, polinomio

# Integrate the function from 1 to 3 with 5 points
result = integrate_function(polinomio, 1, 3, 5)
print(f"Result: {result}")

# Find the optimal number of points
from cuadrature import find_optimal_N
best_N, best_value, difference = find_optimal_N()
print(f"Optimal N: {best_N}, Value: {best_value}")
