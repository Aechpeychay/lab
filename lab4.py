from math import *
def f(x):
	return pow(x, 2) + 8 * exp(0.55 * x)
def fib(n):
	if n in (0, 1) or n < 0:
		return 1
	return fib(n - 1) + fib(n - 2)
a = -2
b = 0
n = input("number of itarations = ")
n = int(n)
orgn_n = n
x1 = a + (b - a) * fib(n-2) / fib(n) 
x2 = a + (b - a) * fib(n-1) / fib(n)
y1 = f(x1)
y2 = f(x2)
while n-2 > 0:
	if y1 <= y2: 
		b = x2
		x2 = x1
		y2 = y1
		x1 = a + b - x2 
		y1 = f(x1)
	else: 
		a = x1
		x1 = x2
		y1 = y2
		x2 = a + b - x1
		y2 = f(x2)	
	n = n - 1
span = (b-a)/fib(orgn_n) 
if y1 < y2:	
	print("local span from :" +  str(x1 - span) + " to " + str(x1 + span))
	print("x = ", x1)
	print("y = ", y1)
else:
	print("local span from :" +  str(x1 - span) + " to " + str(x1 + span))
	print("x = ", x2)
	print("y = ", y2)
