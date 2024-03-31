from math import *
def f(x1, x2, x3, x4):
    return pow((x1 - x2),2) + 4*pow((x3 - x4),2) + pow((x2 - 6*x3),4) + 2*pow((x1 - x4),2)
def min(x1, x2, x3, x4):
	a = -1.0
	b = 3.0
	l = b - a
	delta = 0.001
	while(l/2) > delta:
		x1 = (a+b)/2
		l = b - a
		fx1 = f(x1, x2, x3, x4)
		x1_1 = a + l/4
		x1_2 = b - l/4
		fx1_1 = f(x1_1, x2, x3, x4)
		fx1_2 = f(x1_2, x2, x3, x4)
		if fx1_1 < fx1:
			b = x1
			x1 = x1_1
		else:
			if fx1_2 < fx1:
				a = x1
				x1 = x1_2
			else:
				a = x1_1
				b = x1_2
	return x1
x_check = 8.0
x1_start = 2.0
x2_start = 2.0
x3_start = 2.0
x4_start = 2.0
while abs(x_check - x4) >= 0.001:
	x_check = x4
	x1 = min(x1, x2_start, x3_start, x4_start)
	x1_start = x1
	x2 = min(x2, x1_start, x3_start, x4_start)
	x2_start = x2
	x3 = min(x3, x1_start, x2_start, x4_start)
	x3_start = x3
	x4 = min(x4, x1_start, x2_start, x3_start)
	x4_start = x4
print("Минимум на данном отрезке: ", x1, x2, x3, x4, f(x1,x2,x3,x4))
	x4 = min(x1, x2, x3, x4)
print("Минимум на данном отрезке: ", x1, x2, x3, x4, function(x1,x2,x3,x4))
