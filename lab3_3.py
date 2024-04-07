from scipy.optimize import minimize_scalar
from scipy.optimize import minimize
import numpy as np

eps = 0.01

def f(x):
    return pow((x[0] - x[1]), 2) + 4 * pow((x[2] - x[3]), 2) + pow((x[1] - 6 * x[2]), 4) + 2 * pow((x[0] - x[3]), 2)

def grad_f(x):
    return np.array([
        14*x[0] - 6*x[1] - 8*x[3],
        -6*x[0] + 6*x[1] + 4*(x[1] + 26*x[2])**3,
        2*x[2] - 2*x[3] + 104*(x[1] + 26*x[2])**3,
        -8*x[0] - 2*x[2] + 10*x[3]
    ])


def conjugate_gradient(f, grad_f, x0, eps, max_iter=1000):
    x = np.array(x0, dtype=float)
    g = -grad_f(x)
    d = g.copy()
    for i in range(max_iter):
        def objective(alpha):
            return f(x + alpha * d)
        alpha = 1
        while f(x + alpha * d) > f(x) - alpha * 0.0001 * np.dot(g, d):
            alpha *= 0.5
        x_new = x + alpha * d
        g_new = -grad_f(x_new)
        beta = np.dot(g_new, g_new) / np.dot(g, g)
        d = g_new + beta * d
        x, g = x_new, g_new
        if np.linalg.norm(g) < eps:
            print(i)
            break
    return x

for e in range(4):
    x0 = [1.0, 1.0, 1.0, 1.0]
    x_opt = conjugate_gradient(f, grad_f, x0, eps)
    for i in x_opt:
        print(format(abs(i), '.16f'))
    print(format(f(x_opt), '.20f'))
    print (eps, '\n')
    eps /= 100
