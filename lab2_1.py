from math import *

def f(x1, x2, x3, x4):
	(x1 - x2)^2 + 4*(x3 - x4)^2 + (x2 - 6 * x3)^4 + 2*(x1 - x4)^2
def min():
	a = 0.1
	b = 1                                                                                          
    delta = 0.001              
    error_delta = 1                                                                                 
    lam = (sqrt(5) - 1)/2                                                                            
    x1 = a + (1 - lam)*(b - a)                                                                       
    x2 = a + lam*(b - a)                                                                             
    fx1 = f(x1)                                                                                      
    fx2 = f(x2)                                                                                      
    n = 0                                                                                            
    while error_delta > delta:                                                                       
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
    return (a+b)/2  
array = list(map(int, input().split()))
n = 4
k = 1
i = 1
eps = 0.01
while()

