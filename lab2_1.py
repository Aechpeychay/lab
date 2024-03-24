from math import *
#import numpy as np # https://ruclient.ru/metod-pokoordinatnogo-spuska-na-python/
def f(x1, x2, x3, x4):
	return (x1 - x2)^2 + 4*(x3 - x4)^2 + (x2 - 6 * x3)^4 + 2*(x1 - x4)^2
def min(func, f_x1, f_x2, f_x3): #lab3 f - fix
	a = 0.1
	b = 1                                                                                          
    delta = 0.001              
    error_delta = 1                                                                                 
    lam = (sqrt(5) - 1)/2                                                                            
    x1 = a + (1 - lam)*(b - a)                                                                       
    x2 = a + lam*(b - a)                                                                             
    fx1 = func(x1)
	fx2 = func(x2)   
	n = 0                                                                                            
    while error_delta > delta:                                                                       
        if fx1<fx2:                                                                                 
            b = x2                                                                                   
            x2 = x1                                                                                  
            fx2 = fx1                                                                                
            x1 = a + b - x2                                                                          
            fx1 = func(x1)
		else:                                                                                        
            a = x1                                                                                   
            x1 = x2                                                                                  
            fx1 = fx2                                                                                
            x2 = a + b - x1                                                                          
            fx2 = func(x2)
			error_delta = (b - a)/2
		return (a+b)/2  
x_arr = [1,1,1,1]
eps = 0.01
k = 1
i = 1
n = 4
while True:
	xk = 0
	xk_p_1 = 0
	j = 0
	xk = min(lambda x, f_x1, f_x2, f_x3: f(x1))	#pass a multyple const and 1 var
	xk_p_1 =  
	if abs(xk_p_1 - xk) <= eps:
		break
	else if i < n:
		i = i+1
	else:
		i = 1
		k = k + 1
