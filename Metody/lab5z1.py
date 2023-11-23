import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def sin_1_over_x(x):
    x[x == 0] = 1e-10
    return np.sin(1 / x)

def exp_cos_x(x):
    return np.exp(np.cos(x))

x = np.arange(-np.pi, np.pi, 0.4)
y_sin = sin_1_over_x(x)
y_exp = exp_cos_x(x)

x_interp = np.arange(-np.pi, np.pi, 0.08)
metody = ['linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic']

def interpolacje(x, y, x_interp, methods, funkcja):
    plt.figure(figsize=(15, 10))
    for i, method in enumerate(methods, 1):
        f = interp1d(x, y, kind=method, fill_value="extrapolate")
        y_interp = f(x_interp)

        plt.subplot(2, 3, i)
        plt.plot(x, y, 'o', label='Dane wejściowe')
        plt.plot(x_interp, y_interp, '-', label=method)
        plt.title(f'Metoda: {method}')
        plt.legend()

    plt.suptitle(f'Interpolacja dla funkcji {funkcja}')
    plt.show()

print(f"sin(1/x) = {y_sin}\n")
print(f"cos(x) = {y_exp}")
interpolacje(x, y_sin, x_interp, metody, "sin(1/x)")

interpolacje(x, y_exp, x_interp, metody, "exp(cos(x))")
