import numpy as np


def estimate_coef(x, y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)

    SS_xy = n * np.sum(y*x) - np.sum(x) * np.sum(y)
    SS_xx = n * np.sum(x*x) - np.sum(x) * np.sum(x)

    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_1, b_0)


def main():

    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    b = estimate_coef(x, y)

    print(b)
    print("{:.2f} {:.2f}".format(b[0], b[1]))

    # plotting regression line
    # plot_regression_line(x, y, b)


if __name__ == "__main__":
    main()


'''
sumx = sumy = sumx2 = sumxy = 0 # Initial value of summation variables
for i in range(N):
    sumx += X[i]
    sumy += Y[i]
    sumx2 += X[i]**2
    sumxy += X[i]*Y[i]
meanx = sumx / N
meany = sumy / N

a1 = (N*sumxy - sumx*sumy) / (N*sumx2 - sumx**2)
a0 = meany - a1 * meanx

'''
