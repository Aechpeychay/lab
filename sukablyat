from math import *
def f(x1, x2, x3, x4):
    return (x1 - x2)^2 + 4 * (x3 - x4)^2 + (x2 - 6 * x3)^4 + 2*(x1 - x4)^2
def min(x1, x2, x3, x4):
	a = 3.0
	b = 8.0
	l = b - a
	delta = 0.001
	while(l/2) > delta:
		x0 = (a+b)/2
		l = b - a
		fx0 = f(x0, x2, x3, x4)
		x1_1 = a + l/4
		x2_1 = b - l/4
		fx1_1 = f(x1_1, x2, x3, x4)
		fx2_1 = f(x2_1, x2, x3, x4)
		if fx1_1 < fx0:
			b = x0
			x0 = x1_1
		else:
			if fx2_1 < fx0:
				a = x0
				x0 = x2_1
			else:
				a = x1_1
				b = x2_1
x_check = 8.0
x1 = 5.0
x2 = 5.0
x3 = 5.0
x4 = 5.0
while abs(x_check - x4) >= 0.001:
	x_check = x4
	x1 = min(x1, 5.0, 5.0, 5.0)
	x2 = min(x1, x2, 5.0, 5.0)
	x3 = min(x1, x2, x3, 5.0)
	x4 = min(x1, x2, x3, x4)
print("Минимум на данном отрезке: ", x1, x2, x3, x4, function(x1,x2,x3,x4))
