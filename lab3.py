from math import *

def f(x):
	return pow(x,2) + 8 * exp(0.55 * x)

a = -2
b = 0
delta = 0.001
error_delta = 1
lam = (sqrt(5) - 1)/2
x1 = a + (1 - lam)*(b - a)
x2 = a + lam*(b - a)
fx1 = f(x1)
fx2 = f(x2)
n = 0
while error_delta > delta:
	n = n + 1
	if fx1<fx2:
		b = x2 
		x2 = x1
		fx2 = fx1
		x1 = a + b - x2
		fx1 = f(x1)
	else:
		a = x1
		x1 = x2
		fx1 = fx2
		x2 = a + b - x1
		fx2 = f(x2)
	error_delta = (b - a)/2
print("x1 = " + str(x1))
print("x* = " + str((a+b)/2))
print("x2 = " + str(x2))
print("n = " + str(n))
