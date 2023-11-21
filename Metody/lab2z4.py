import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2
    

def funkcja(f, xp, xk ,k, opcja):
    x = [i for i in np.arange(xp, xk, k)]
    y = [f(1) for i in np.arange(xp, xk, k)]
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Wykres f(x) = x**2')
    if opcja == 1:
        plt.grid(visible = True, axis = 'both')
        plt.plot(x, y, 'g.')
    else:
        plt.plot(x,y)
    plt.show()
    
funkcja(f, -2, 2, 0.1, 0)
