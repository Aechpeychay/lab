import numdifftools as nd
import numpy as np

n = 4
eps = 0.01
a = 0.00001

def f(x):
    return pow((x[0] - x[1]), 2) + 4 * pow((x[2] - x[3]), 2) + pow((x[1] - 6 * x[2]), 4) + 2 * pow((x[0] - x[3]), 2)

def sum_of_diffs(x):
    df_dx0 = 6 * (x[0] - x[1]) + 8 * (x[1] + 26 * x[2]) ** 3 + 8 * (x[0] - x[3])
    df_dx1 = -6 * (x[0] - x[1]) + 8 * (x[1] + 26 * x[2]) ** 3
    df_dx2 = 2 * (x[2] - x[3]) + 104 * (x[1] + 26 * x[2]) ** 3
    df_dx3 = -2 * (x[2] - x[3]) - 8 * (x[1] + 26 * x[2]) ** 3 + 8 * (x[0] - x[3])
    return df_dx0 + df_dx1 + df_dx2 + df_dx3

for e in range(4):
    x = np.array([0.01, 0.01, 0.01, 0.01])

    for i in range(1, 100):
        x_pr = x.copy()
        grad = np.array(nd.Gradient(f)(x))
        a_grad = np.linalg.norm(grad)
        x = x - a * (grad / a_grad)
        if (sum_of_diffs(x) < eps):
            print(i)
            break
    print(x)
    print(format(f(x), '.16f'))
    print (eps, '\n')
    eps /= 100
