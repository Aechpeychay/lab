import numpy as np

n = 4
eps = 0.01
x0 = [2, 2, 2, 2]
def f(x):
    return pow((x[0] - x[1]), 2) + 4 * pow((x[2] - x[3]), 2) + pow((x[1] - 6 * x[2]), 4) + 2 * pow((x[0] - x[3]), 2)

def initialize_simplex(initial_point, a = 1):
    simplex = np.zeros((n + 1, n))
    simplex[0] = initial_point
    sig1 = ((np.sqrt(n + 1) + n - 1) / (n * np.sqrt(2))) * a
    sig2 = ((np.sqrt(n + 1) - 1) / (n * np.sqrt(2))) * a
    for i in range(1, n + 1):
        for j in range(n):
            if (j != i):
                simplex[i][j] = initial_point[j] + sig1
            else:
                simplex[i][j] = initial_point[j] + sig2
    return simplex

def simplex_method(func, initial_point, eps, max_iter=1000):
    a = 1
    simplex = initialize_simplex(initial_point)
    simplex_history = np.zeros((max_iter * 5, n))
    for i in range(n):
        simplex_history[i] = simplex[i]
    for i in range(max_iter):
        simplex = sorted(simplex, key=func)
        best = simplex[0]
        worst = simplex[-1]
        centroid = np.mean(simplex[:-1], axis=0)
        reflected = centroid + (centroid - worst)
        if func(best) <= func(reflected) < func(simplex[-2]):
            simplex[-1] = reflected
        elif func(reflected) < func(best):
            expanded = centroid + 2 * (reflected - centroid)
            simplex[-1] = expanded if func(expanded) < func(reflected) else reflected
        else:
            contracted = centroid + 0.5 * (worst - centroid)
            simplex[-1] = contracted if func(contracted) < func(worst) else worst
        if np.std([func(point) for point in simplex]) < eps:
            print(i + 1)
            break
        for j in range((i + 1) * 5, (i + 2) * 5):
            simplex_history[j] = simplex[(j % 5)]
        if (i > 4):
            for j in range((i - 4) * 5, (i - 3) * 5):
                for k in range((i + 1) * 5, (i + 2) * 5):
                    for l in range(0, n):
                        if simplex_history[j][l] != simplex_history[k][l]:
                            break
                        if n == 3:
                            a *= 0.5
                            simplex = initialize_simplex(best, a)
    return sorted(simplex, key=func)[0]

for e in range(4):
    result = simplex_method(f, x0, eps)
    for i in result:
        print(format(i, '.16f'))
    print(format(f(result), '.16f'))
    print (eps, '\n')
    eps /= 100

