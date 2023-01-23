from math import pi, sin


def f(x): return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5


a = 0
b = 0.8

n = 2
h = (b - a) / n

# odd -> 4
# even -> 2

S = (f(a) + f(b))
for i in range(1, n, 2):
    S += 4 * f(a + i*h)
for i in range(2, n, 2):
    S += 2 * f(a + i*h)
I = 1/3 * h * S

print("Integral of the equation, I = %f" % I)
