from math import *

def f(x):
	print(x)
	return pow(x,2) + 8 * exp(0.55*x)
def df(x):
	return 2*x+((22*exp((11/20)*x))/5)
def disp(a,c,b):
	print("a = " + str(a))
	print("c = " + str(c))
	print("b = " + str(b))
a = -2
b = 0
eps = float(input("epsilon: "))
y1 = f(a)
y2 = f(b)
z1 = df(a)
z2 = df(b)
while 1:
	if b - a <= 2 * eps:
		x = (a+b)/2
		y = f(x)
		disp(a,x,b)
		break
	else:
		c = ((b*z2-a*z1)-(y2-y1))/(z2 - z1)
		y = f(c)
		z = df(c)
		if z == 0:
			x = c
			y = y
			disp(a,x,b)
			break
		if z < 0:
			a = c
			y1 = y
			z1 = z
		else:
			b = c
			y2 = y
			z2 = z
