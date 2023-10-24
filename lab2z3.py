import numpy as np

def f(x):
    try:
        return 1/x
    except ZeroDivisionError:
        print("Nie dziel przez zero!")
        return 0   
    

def suma(f, xp, xk, krok): 
    wartosc = 0
    for i in np.arange(xp, xk, krok):
        wartosc += f(i)
        # print(f(i))
    print(wartosc)
    
def iloczyn(f, xp, xk, krok): 
    wartosc = 1
    for i in np.arange(xp, xk, krok):
        wartosc = wartosc * f(i)
        # print(f(i))
        
    print(wartosc)


suma(f, -3.14, 3.14, 0.01)
suma(np.sin, -3.14, 3.14, 0.01)
iloczyn(f, -3.14, 3.14, 0.01)
iloczyn(np.sin, -3.14, 3.14, 0.01)