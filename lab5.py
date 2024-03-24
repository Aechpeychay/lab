from math import *
def der_f(x):
	return 2*x+((22*exp((11/20)*x))/5)
def mid(a,b):
	return (a+b)/2
eps = float(input("epsilon: "))
a = -2
b = 0
d_x0 = 0
x0 = 0
while abs(der_f(x0)) > eps:
	x0 = (a+b)/2
	if der_f(x0) < 0:
		a = x0
	else: 
		b = x0	
print("a = " + str(a))
print("b = " + str(b))
print("x* = " + str(x0))
