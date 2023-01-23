from numpy import array, fabs, linalg, zeros


def gauss_jordan():

    coff = array([
        [2, -1, 3],
        [1, 1, 1],
        [1, -1, 1]
    ], float)

    b = array([9, 6, 2], float)

    n = len(b)
    # print(linalg.solve(coff, b))

    for k in range(n):

        # Division of pivot
        pivot = coff[k][k]

        for j in range(k, n):
            coff[k][j] /= pivot
        b[k] /= pivot

        for i in range(n):
            if i == k or coff[i][k] == 0:
                continue
            factor = coff[i][k]

            for j in range(k, n):
                coff[i][j] -= factor * coff[k][j]
            b[i] -= factor * b[k]

    print(coff)
    print(b)


gauss_jordan()
