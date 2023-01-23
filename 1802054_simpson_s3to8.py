from math import pi, sin


def f(x): return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5


a = 0
b = 0.8

n = 6
h = (b - a) / n


# non 3 multiple -> 3
# 3 multiple -> 2

S = (f(a) + f(b))
for i in range(1, n, 3):
    S += 3 * (f(a + i*h) + f(a + (i+1)*h))
for i in range(3, n, 3):
    S += 2 * f(a + i*h)
I = 3/8 * h * S

print("Integral of the equation, I = %f" % I)
