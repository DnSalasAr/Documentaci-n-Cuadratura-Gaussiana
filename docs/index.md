# Documentación de cuadratura gaussiana

Se busca explicar y ejemplificar el uso de la cuadratura gaussiana aplicada a diferentes funciones. En esta documentación se usará la función $f(x)=-sin(2x) \times x^2 + x^6$ y se va integrar en un intervalo de $[1,3]$. Este método empleado calcula númericamente la integral, entonces es una aproximación. Sin embargo, estas aproximaciones pueden llevar a resultados exactos por el error de punto flotante.

\[ \int_{a}^{b} x^6-sin(2x)x^2 \,dx \]

Con otras herramientas, como WolframAlpha, se sabe que la integral es igual a $2186/7 + 1/4 (-cos(2) + 17 cos(6) + 2 sin(2) - 6 sin(6))$. Este resultado es aproximadamente $317.34424667382635655$.


Los resultados obtenidos son que el número más óptimo de puntos para calcular esta integral son 9 (N=9), y dando un valor aproximado de $317.34442466738264$.
