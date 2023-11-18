import numpy as np
import pylab

def interpolacja_lagrange(x,y, xval):
    products = 0
    yval = 0
    for i in range(len(x)):
        products = y[i]
        for j in range(len(x)):
            if i != j:
                products *= (xval - x[j])/(x[i] - x[j])
        yval += products
    return yval

x_exp = []
x_exp.append([i for i in np.arange(-3.14, 3.14, 0.1)])
x_exp.append([np.exp(np.cos(i)) for i in x_exp[0]])
print(x_exp)
print(interpolacja_lagrange(x_exp[0], x_exp[1], 0.5))

x_sin = []
x_sin.append([i for i in np.arange(-3.14, 3.14, 0.1)])
x_sin.append([np.sin(i/1) for i in x_sin[0]])
print(x_sin)
print(interpolacja_lagrange(x_sin[0], x_sin[1], 0.5))

x_exp_val = [i for i in np.arange(-3.14, 3.14, 0.1)]
y_exp_val = []
for xv in x_exp_val:
    y_exp_val.append(interpolacja_lagrange(x_exp[0], x_exp[1], xv))

pylab.figure(figsize=(16, 8))
pylab.subplot(1, 2, 1)
pylab.plot(x_exp[0], x_exp[1], 'o', label='Oryginalne dane')
pylab.plot(x_exp_val, y_exp_val, '.-', label='Interpolowane dane')
pylab.title('Interpolacja exp(cos(x))')
pylab.legend()

x_sin_val = [i for i in np.arange(-3.14, 3.14, 0.1)]
y_sin_val = []
for xv in x_sin_val:
    y_sin_val.append(interpolacja_lagrange(x_sin[0], x_sin[1], xv))
    
pylab.subplot(1, 2, 2)
pylab.plot(x_sin[0], x_sin[1], 'o', label='Oryginalne dane')
pylab.plot(x_sin_val, y_sin_val, '.-', label='Interpolowane dane')
pylab.title('Interpolacja sin(x)')
pylab.legend()
