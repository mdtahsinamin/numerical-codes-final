from numpy import array, linalg, zeros

X = [0, 1, 2, 3, 4, 5]
Y = [2, 8, 14, 28, 39, 62]

X = array(X, float)
Y = array(Y, float)

N = len(X)
n = 2

A = zeros((n+1, n+1))
B = zeros(n+1)
a = zeros(n+1)

A[0, 0] = N
for row in range(n+1):

    for col in range(n+1):
        if row == 0 and col == 0:
            continue

        A[row, col] = sum(X**(row+col))

    B[row] = sum(X**row * Y)

a = linalg.solve(A, B)


print("The polynomial equation :")
print('y = %f' % a[0], end=' ')
for i in range(1, n+1):
    print('%+f x^%d' % (a[i], i), end=' ')
print()
