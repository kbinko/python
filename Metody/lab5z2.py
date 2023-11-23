import numpy as np
import matplotlib.pyplot as plt

def sin_1_przez_x(x):
    x[x == 0] = 1e-10
    return np.sin(1 / x)

def exp_cos_x(x):
    return np.exp(np.cos(x))

def polynomial_interp(x, y, x_interp):
    wielomian = np.polyfit(x, y, 9)

    y_interp = np.polyval(wielomian, x_interp)

    return y_interp

x = np.arange(-np.pi, np.pi, 0.4)
y_sin = sin_1_przez_x(x)
y_exp = exp_cos_x(x)

x_gesto = np.arange(-np.pi, np.pi, 0.08)

y_sin_interp = polynomial_interp(x, y_sin, x_gesto)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, y_sin, 'o', label='Dane oryginalne sin(1/x)')
plt.plot(x_gesto, y_sin_interp, '-', label='Interpolacja wielomianowa')
plt.title('Interpolacja sin(1/x)')
plt.legend()

y_exp_interp = polynomial_interp(x, y_exp, x_gesto)
plt.subplot(1, 2, 2)
plt.plot(x, y_exp, 'o', label='Dane oryginalne exp(cos(x))')
plt.plot(x_gesto, y_exp_interp, '-', label='Interpolacja wielomianowa')
plt.title('Interpolacja exp(cos(x))')
plt.legend()

plt.show()

print(f"sin(1/x) = {y_sin}")
print(f"cos(x) = {y_exp}")