from math import pi, sin


def f(x): return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5


a = 0
b = 0.8

n = 10
h = (b - a) / n


S = 0.5 * (f(a) + f(b))
for i in range(1, n):
    S += 2 * f(a + i*h)
I = h * S

print("Integral of the equation, I = %f" % I)
