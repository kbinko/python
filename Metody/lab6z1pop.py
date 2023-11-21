import numpy as np
import matplotlib.pyplot as plt


def linear_regression(x, y):
    N = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x*y)
    b = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x**2)
    a = (sum_y - b * sum_x) / N
    return a, b

x_linear = np.arange(-20, 20)
y_linear = 3 * x_linear + 5 + np.random.normal(scale=10, size=len(x_linear))

a_linear, b_linear = linear_regression(x_linear, y_linear)


plt.scatter(x_linear, y_linear, color='blue', label='Dane liniowe')
plt.plot(x_linear, a_linear + b_linear * x_linear, color='red', label=f'Linia regresji: y = {a_linear:.2f} + {b_linear:.2f}x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dobrze dopasowana regresja liniowa')
plt.legend()
plt.show()

a_linear, b_linear

