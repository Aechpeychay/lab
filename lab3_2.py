import numdifftools as nd
import numpy as np

n = 4
eps = 0.01

def f(x):
    return pow((x[0] - x[1]), 2) + 4 * pow((x[2] - x[3]), 2) + pow((x[1] - 6 * x[2]), 4) + 2 * pow((x[0] - x[3]), 2)

for e in range(4):
    x = np.array([1.0, 1.0, 1.0, 1.0])
    for i in range(1, 1000):
        x_pr = x.copy()
        dk = -1 * np.array(nd.Gradient(f)(x))
        a = 1.0
        min = [a, f(x + a * dk)]
        for j in range(1, 1000):
            a /= 2
            if f(x + a * dk) < min[1]:
                min = [a, f(x + a * dk)]
        x = x + min[0] * dk
        if (np.linalg.norm(x_pr) < eps):
            print(i)
            break
    print(x)
    print(format(f(x), '.16f'))
    print (eps, '\n')
    eps /= 100
