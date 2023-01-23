'''
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
print(my_list[:5])


def f(x): return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5


print(f(0.8))
def x(a, b): return a * b


print(x(5, 6))
'''

from math import cos


def func(x):
    return 3*x - cos(x) - 1


def bisection(a, b):

    while (1):

        c = (a+b)/2

        if (func(a) * func(c) == 0.00):
            break

        if (func(c)*func(a) < 0.00):
            b = c
        else:
            a = c

    print("The value of root is : ", "%.4f" % c)


a = 0
b = 1
bisection(a, b)
