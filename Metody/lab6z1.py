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

x = np.arange(-20, 20)
y = 0.5 * x**3 + 1.5 * x**2 - 2.5 * x + 69 + np.random.normal(scale=200, size=len(x))

# x = np.arange(-20, 20)
# y = 3 * x + 5 + np.random.normal(scale=10, size=len(x))

a, b = linear_regression(x, y)

print(f"Współczynniki regresji: a = {a}, b = {b}")

y_pred = a + b * x

absolute_errors = np.abs(y - y_pred)
relative_errors = absolute_errors / np.abs(y)
mean_absolute_error = np.mean(absolute_errors)
mean_relative_error = np.mean(relative_errors)
print(f"Średni błąd bezwzględny: {mean_absolute_error}")
print(f"Średni błąd względny: {mean_relative_error * 100:.2f}%")

plt.scatter(x, y, color='blue', label='Dane')
plt.plot(x, a + b * x, color='red', label=f'Linia regresji: y = {a:.2f} + {b:.2f}x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresja liniowa')
plt.legend()
plt.show()

#Średni błąd bezwzględny i względny jest wysoki,
# ponieważ użyliśmy aproksymacji liniowej do zbioru danych,
# które są nieliniowe, co sprawia że aproksymacja nie jest dokładna
