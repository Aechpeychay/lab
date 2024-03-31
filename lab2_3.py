import numpy as np

n = 4
initial_simplex = [[0.5, 0.5, 0.5, 0.5], [1, 1, 1, 1], [1.5, 1.5, 1.5, 1.5], [2.5, 2.5, 2.5, 2.5]]
eps = 0.001

def f(x):
    return pow((x[0] - x[1]), 2) + 4 * pow((x[2] - x[3]), 2) + pow((x[1] - 6 * x[2]), 4) + 2 * pow((x[0] - x[3]), 2)


def nelder_mead(f, initial_simplex, eps, max_iter=1000):
    alpha = 1
    gamma = 2
    beta = 0.5
    simplex = np.array(initial_simplex)
    values = np.array([f(point) for point in simplex])
    for i in range(max_iter):
        order = np.argsort(values)
        simplex = simplex[order]
        values = values[order]
        x_bar = np.mean(simplex[:-1], axis=0)
        x_r = x_bar + alpha * (x_bar - simplex[-1])
        f_r = f(x_r)
        if f_r < values[-2]:
            x_e = x_bar + gamma * (x_r - x_bar)
            f_e = f(x_e)
            if f_e < f_r:
                simplex[-1] = x_e
                values[-1] = f_e
            else:
                simplex[-1] = x_r
                values[-1] = f_r
        else:
            x_c = x_bar + beta * (simplex[-1] - x_bar)
            f_c = f(x_c)
            if f_c < values[-1]:
                simplex[-1] = x_c
                values[-1] = f_c
            else:
                for i in range(1, n + 1):
                    simplex[i] = simplex[0] + sigma * (simplex[i] - simplex[0])
                    values[i] = f(simplex[i])
        if np.max(np.abs(simplex[1:] - simplex[0])) < eps:
            print(i)
            break
    best_index = np.argmin(values)
    return simplex[best_index]

for e in range(4):
    best_point = nelder_mead(f, initial_simplex, eps)
    for i in best_point:
        print(format(i, '.16f'))
    print(format(f(best_point), '.35f'))
    print (eps, '\n')
    eps /= 100
