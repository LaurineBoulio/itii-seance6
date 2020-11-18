
#Exercice 1
import numpy as np
import math

def integrale(f, a, b, n):
    integrale = 0
    k=a;
    while(k < b):
        largeur = (b-a)/n
        hauteur = f(a + k*(b-a)/n)
        aire = largeur * hauteur
        integrale += aire
        k+=n
 
    return integrale

f = lambda x : 3*x**3 + 2*x - 1
print(integrale(f,0,10,0.001)) 

g = lambda x : math.cos(1/x)
print(integrale(g,0,10,0.001)) 

#correction
from sympy import *
def calculate_dx (a, b, n):
    return (b-a)/float(n)

def f(x):
    return 3*x**2

def integrale (f, a, b, n):
    Total=0
    dx=calculate_dx (a, b, n)
    for i in range(1,n+1):
        fi=f(a+i*(dx))
        Total=Total+fi
    integral=Total*dx
    return(integral)

integrate(t**2*sin(t), t)

import numpy as np

def f(x):
    return x**2+x

n=10
a=0
b=1
integral_real=integrate(x**2+x, (x,a,b))
higherror=True
step=100
                        
while (higherror):
    integral_num=integrale(f,0,1,n)
    if np.abs(integral_num-integral_real)<10**-4:
        higherror=False
    n=n+step



print(n)   

#Exercice 2


	#question 2
def trapezes(f,a,b,N):
	pas = (b-a)/NameError