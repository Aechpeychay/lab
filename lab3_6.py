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

def dfp_corrected(f, grad_f, x0, eps, max_iter=100):
    x = np.array(x0, dtype=float)
    H = np.eye(len(x0))
    for i in range(max_iter):
        grad = grad_f(x)
        if np.linalg.norm(grad) < eps:
            print(i)
            break
        p = -H.dot(grad)
        def objective(alpha):
            return f(x + alpha * p)
        res = minimize_scalar(objective, method='golden')
        alpha = res.x
        x_new = x + alpha * p
        delta_x = x_new - x
        delta_grad = grad_f(x_new) - grad
        dg = delta_grad.reshape(-1, 1)
        dx = delta_x.reshape(-1, 1)
        Hdg = H.dot(dg)
        H = H + (dx @ dx.T) / (dx.T @ dg) - (Hdg @ Hdg.T) / (dg.T @ Hdg)
        x = x_new
    return x

for e in range(4):
    x0 = [1.0, 1.0, 1.0, 1.0]
    x_opt = dfp_corrected(f, grad_f, x0, eps)
    for i in x_opt:
        print(format(i, '.10f'))
    print(format(f(x_opt), '.20f'))
    print (eps, '\n')
    eps /= 100
