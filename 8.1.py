import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy.integrate import quad

# Определение функции
def f(x):
    return (x - 5)**2 * np.cos(x**2 - 7)

# Определение отрезка
x_values = np.linspace(0, 5, 100)
y_values = f(x_values)

# 2. Найти наибольшее и наименьшее значение функции на отрезке и отобразить точкой
min_point = (x_values[np.argmin(y_values)], np.min(y_values))
max_point = (x_values[np.argmax(y_values)], np.max(y_values))

# Построение графика функции
plt.figure(figsize=(12, 8))
plt.plot(x_values, y_values, label="График 1")
plt.plot(*min_point, "o", color="r", label="Min точка")
plt.plot(*max_point, "o", color="g", label="Max точка")

# Разделение графиков функции и её первой производной
plt.title("График 1")
plt.legend()
plt.grid(True)
plt.show()

# График первой производной
plt.figure(figsize=(12, 8))
derivative_1 = np.vectorize(lambda x: derivative(f, x, dx=1e-6, n=1))
plt.plot(x_values, derivative_1(x_values), label="График 2 (1-я производная)")
plt.title("График 2 (1-я производная)")
plt.legend()
plt.grid(True)
plt.show()

# График нормали и касательной
def tangent_line(x, x0, y0):
    slope = derivative(f, x0, dx=1e-6, n=1)
    return y0 + slope * (x - x0)

def normal_line(x, x0, y0):
    slope = derivative(f, x0, dx=1e-6, n=1)
    return y0 - 1/slope * (x - x0)

x_tangent_extended = np.linspace(0, 5, 200)
y_tangent_extended = tangent_line(x_tangent_extended, *min_point)

x_normal_extended = np.linspace(0, 5, 200)
y_normal_extended = normal_line(x_normal_extended, *min_point)

# Построение графика касательной и нормали
plt.figure(figsize=(12, 8))
plt.plot(x_values, y_values, label="График 1")
plt.plot(x_tangent_extended, y_tangent_extended, '--', label="Касательная")
plt.plot(x_normal_extended, y_normal_extended, '--', label="Нормаль")
plt.title("График 1 с Касательной и Нормалью")
plt.legend()
plt.grid(True)
plt.show()

# 4. Построить касательное расслоение (график 4)
tangent_layers = [tangent_line(x_values, x_val, y_val) for x_val, y_val in zip(x_values, y_values)]

plt.figure(figsize=(12, 8))
plt.plot(x_values, tangent_layers, '--', label="График 4 (Касательное расслоение)")
plt.title("График 4 (Касательное расслоение)")
plt.legend()
plt.grid(True)
plt.show()

# 5. Найти длину кривой через интеграл
curve_length, _ = quad(lambda x: np.sqrt(1 + derivative(f, x, dx=1e-6, n=1)**2), 0, 5)

print(f"Длина кривой: {curve_length:.4f}")
