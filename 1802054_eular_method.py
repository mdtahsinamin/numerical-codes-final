from math import exp


def dy(x, y): return -2*x**3 + 12*x**2 - 20*x + 8.5


def f(x, y): return -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1


x = 0
xn = 4
y = 1

h = 0.5
n = int((xn-x)/h)


print('x \t\ty(Euler) \ty(Analytical)')
print('%f \t%f \t%f' % (x, y, f(x, y)))

for i in range(n):
    y += dy(x, y)*h
    x += h
    print('%f \t%f \t%f' % (x, y, f(x, y)))
