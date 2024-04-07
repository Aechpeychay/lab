from scipy.optimize import minimize
import numpy as np

eps = 0.001

def f(x):
    return pow((x[0] - x[1]), 2) + 4 * pow((x[2] - x[3]), 2) + pow((x[1] - 6 * x[2]), 4) + 2 * pow((x[0] - x[3]), 2)

def grad_f(x):
    return np.array([
        14*x[0] - 6*x[1] - 8*x[3],
        -6*x[0] + 6*x[1] + 4*(x[1] + 26*x[2])**3,
        2*x[2] - 2*x[3] + 104*(x[1] + 26*x[2])**3,
        -8*x[0] - 2*x[2] + 10*x[3]
    ])

def hessian_f(x):
    x1, x2 = x[1], x[2]
    return np.array([[14, -6, 0, -8],
                    [-6, 12*(x1 + 26*x2)**2 + 6, 312*(x1 + 26*x2)**2, 0],
                    [0, 312*(x1 + 26*x2)**2, 8112*(x1 + 26*x2)**2 + 2, -2],
                    [-8, 0, -2, 10]])

#В программе используется модифицированный метод Ньютона
def newton_method(f, grad_f, hessian_f, x0, eps, max_iter=1000):
    x = np.array(x0)
    for i in range(max_iter):
        grad = grad_f(x)
        H = hessian_f(x)
        delta_x = np.linalg.solve(H, -grad)
        x = x + delta_x
        if np.linalg.norm(grad) < eps:
            print(i)
            break
    return x

for e in range(4):
    x0 = [1.0, 1.0, 1.0, 1.0]
    x_opt = newton_method(f, grad_f, hessian_f, x0, eps)
    for i in x_opt:
        print(format(i, '.7f'))
    print(format(f(x_opt), '.16f'))
    print (eps, '\n')
    eps /= 100
