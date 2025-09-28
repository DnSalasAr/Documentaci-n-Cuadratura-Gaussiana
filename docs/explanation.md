# Cuadratura Gaussiana

La idea fundamental se expresa como
\begin{align}
\int_a^b {\rm d}x\, f(x) \approx \sum_{k=1}^{N} w_k\, f(x_k),
\end{align}
donde:
  * $w_k$ representan los *pesos*,
  * $x_k$ son los puntos de muestreo.

Para las fórmulas de Newton–Cotes vistas en la clase anterior:
  * Los puntos de muestreo se encuentran **equispaciados**.
  * Una regla de Newton–Cotes de orden $N$ es *exacta* (sin error) para cualquier polinomio de grado $N$.
  * Un polinomio de orden $N$ aproxima mejor a una función bien comportada que uno de orden $N-1$, gracias al mayor número de grados de libertad.

En contraste, para la cuadratura Gaussiana:
  * Los puntos de muestreo se eligen de manera que **no son equidistantes**, lo que otorga más grados de libertad para una misma discretización en $N$ subintervalos.
  * La regla es exacta para polinomios de grado $(2N - 1)$.
  * En otras palabras, con el mismo número de puntos $N$, se alcanza la precisión de un polinomio de orden $(2N - 1)$.

A continuación, veamos las ventajas y desventajas de emplear cuadraturas Gaussianas para calcular integrales.

* **Ventajas**:
  - Aunque la expresión para estimar el error es complicada, la aproximación mejora con un error que decrece aproximadamente como ${\rm const.}/N^2$ al aumentar el número de subintervalos.
  - Ejemplo: al pasar de $N=10$ a $N=11$, la estimación mejora en un factor cercano a $100$, lo que muestra que la convergencia puede lograrse con pocos puntos de muestreo.

* **Desventajas**:
  - Solo es eficaz cuando la función a integrar es relativamente regular. Si presenta regiones problemáticas, se requieren más puntos de muestreo en dichas zonas.
  - La evaluación precisa del error resulta complicada si se necesita conocerlo con exactitud.

## Polinomios de Legendre

Los polinomios de Legendre forman un sistema ortogonal que puede definirse recursivamente. Cumplen
\begin{align}
\forall (M,N)\in \mathbb{N}^2,\quad \int_{-1}^1 {\rm d}x\, P_N(x) P_M(x) = \frac{2\,\delta_{MN}}{2N+1}.
\end{align}
Obsérvese que están definidos en el intervalo $[-1,1]$.

Se inician con
\begin{align}
P_0(x) = 1,\qquad P_1(x) = x,
\end{align}
y los órdenes superiores se obtienen mediante la relación de recurrencia
\begin{align}
(N+1)P_{N+1}(x) = (2N+1)xP_N(x) - N P_{N-1}(x).
\end{align}
De forma alternativa, también pueden definirse de manera iterativa mediante la fórmula de Rodrigues:
\begin{align}
P_N(x) = \frac{1}{2^N N!}\,\frac{{\rm d}^N}{{\rm d}x^N}\big[(x^2 - 1)^N\big].
\end{align}

Una vez obtenidos los polinomios de Legendre, se determinan sus raíces y se calculan los pesos $w_k$ siguiendo la regla indicada al inicio.  
Este procedimiento puede ser costoso según el método empleado.  
La estrategia típica consiste en calcular previamente los puntos de muestreo $x_k$ y los pesos $w_k$ en el intervalo $[-1,1]$, para luego reescalar estos valores al intervalo de integración deseado $[a,b]$.
\begin{align}
    x_{\mathrm{esc}} &= \frac{b - a}{2}\, x + \frac{a + b}{2} \\
    w_{\mathrm{esc}} &= \frac{b - a}{2}\, w
\end{align}







