### Fórmula de la integral

$$
\int_1^6 x^2 \, dx = \frac{6^3 - 1^3}{3} = 71.67
$$
$$
\int_1^6 x^2 \, dx = \frac{6^3 - 1^3}{3} = 71.67
$$

### Código en Octave

```octave
f = @(x) x.^2;
res = quad(f, 1, 6)
