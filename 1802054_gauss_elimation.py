from numpy import array, fabs, linalg, zeros

'''
System Solution
x + y + z = 9
2x + 5y + 7z = 52
2x + y – z = 0
'''

coff = array([
    [2, -1, 3],
    [1, 1, 1],
    [1, -1, 1]
], float)
b = array([9, 6, 2], float)

n = len(b)
x = zeros(n, float)


# Elimination
for k in range(n - 1):
    if (fabs(coff[k][k]) < 1.0e-12):
        for i in range(k+1, n):
            if (fabs(coff[i][k]) > fabs(coff[k][k])):
                coff[[k, i]] = coff[[i, k]]
                b[[k, i]] = b[[i, k]]
                break

    for i in range(k+1, n):
        if (coff[i][k] == 0):
            continue
        factor = coff[k][k]/coff[i][k]
        for j in range(k, n):
            coff[i][j] = coff[k][j] - coff[i][j] * factor
        b[i] = b[k] - b[i] * factor

print(coff)
print(b)
# Back substitution
x[n - 1] = b[n - 1] / coff[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    sum_ax = 0
    for j in range(i+1, n):
        sum_ax += (coff[i][j]) * x[j]
    x[i] = (b[i] - sum_ax)/coff[i][i]

print(x)
