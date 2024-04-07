import numpy as np
import numdifftools as nd

eps = 0.01

def f(x):
    return pow((x[0] - x[1]), 2) + 4 * pow((x[2] - x[3]), 2) + pow((x[1] - 6 * x[2]), 4) + 2 * pow((x[0] - x[3]), 2)

def grad_f(x):
	df_dx0 = 2 * (x[0] - x[1]) + 4 * (x[0] - x[3])
	df_dx1 = -2 * (x[0] - x[1]) + 4 * (x[1] - 6*x[2])**3
	df_dx2 = 8 * (x[2] - x[3]) - 24 * (x[1]-6*x[2])**3
	df_dx3 = -8 * (x[2] - x[3]) - 4 * (x[0] - x[3])
	return np.array([df_dx0, df_dx1, df_dx2, df_dx3])

def line_search(f, xk, dk):
    alpha_low = 0
    alpha_high = 1
    phi = (1 + np.sqrt(5)) / 2

    while alpha_high - alpha_low > 1e-15:
        alpha1 = alpha_high - (alpha_high - alpha_low) / phi
        alpha2 = alpha_low + (alpha_high - alpha_low) / phi
        if f(xk + alpha1 * dk) < f(xk + alpha2 * dk):
            alpha_high = alpha2
        else:
            alpha_low = alpha1

    return (alpha_low + alpha_high) / 2

def fletcher_reeves(f, grad_f, x0, epsilon, max_iter=1000):
    xk = x0
    gk = -1 * nd.Gradient(f)(xk)
    dk = gk
    iter_count = 0
    while np.linalg.norm(gk) > epsilon and iter_count < max_iter:
        alpha_k = line_search(f, xk, dk)
        xk1 = xk + alpha_k * dk
        gk1 = -grad_f(xk1)
        beta_k1 = np.dot(gk1, gk1) / np.dot(gk, gk)
        dk1 = gk1 + beta_k1 * dk
        xk, gk, dk = xk1, gk1, dk1
        iter_count += 1
    print(iter_count)
    return xk

for e in range(4):
    x0 = np.array([1.0, 1.0, 1.0, 1.0])
    x = fletcher_reeves(f, grad_f, x0, eps)
    for i in x:
        print(format(i, '.7f'))
    print(format(f(x), '.20f'))
    print (eps, '\n')
    eps /= 100
