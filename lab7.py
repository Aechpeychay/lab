from math import * 
def f(x):
	return pow(x,2) + 8 * exp(0.55 * x)
def disp(a,x,b):
    print("a = " + str(a))
    print("x* = " + str(x))
    print("b = " + str(b))
a = -2
c = -1
b = 0
eps = float(input("eps: "))
ya = f(a)
yc = f(c)
yb = f(b)
while True:
	t = c + 0.5 * (pow(b - c, 2) * (ya - yc) - pow(c - a, 2) * (yb - yc))/((b - c) * (ya - yc) + (c - a) * (yb - yc))
	x = t if t != c else (a+c)/2
	y = f(x)
	if x < c:
		print("x<c")
		if y < yc: 
			b = c 
			c = x 
			yb = yc 
			yc = y
		if y > yc: 
			a = x 
			ya = y
		if y == yc: 
			a = x 
			b = c
			c = (x+c)/2
			ya = y
			yb = yc
			yc = f(c)
	else:
		print("x>c")
		if y < yc:
			a = c 
			c = x 
			ya = yc 
			yc = y
		if y > yc: 
			b = x
			yb = y
		if y == yc:
			a = c
			b = x
			c = (x+c)/2
			ya = yc
			yb = y
			yc = f(c)
	if b - a <= eps:
		disp(a,x,b)
		break 
