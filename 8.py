import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sin, cos, diff, lambdify
from sympy import sqrt, integrate

# Задаем переменную
x = symbols('x')

# Задаем функцию
f_expr_1 = sin(x) * cos(x**2 + 5)

# Создаем функцию и компилируем ее с помощью lambdify
f_1 = lambdify(x, f_expr_1, 'numpy')

# Задаем отрезок [a, b]
a, b = 0, 5
x_values_1 = np.linspace(a, b, 1000)
y_values_1 = f_1(x_values_1)

# График 1: Функция и точка экстремума
plt.figure(1)
plt.plot(x_values_1, y_values_1, label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График 1: Функция и точка экстремума')

# График 2: Первая производная
f_prime_1 = lambdify(x, diff(f_expr_1, x), 'numpy')
plt.figure(2)
plt.plot(x_values_1, f_prime_1(x_values_1), label="f'(x)")
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title('График 2: Первая производная')

# График 3: Вторая производная
f_double_prime_1 = lambdify(x, diff(f_expr_1, x, 2), 'numpy')
plt.figure(3)
plt.plot(x_values_1, f_double_prime_1(x_values_1), label="f''(x)")
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.title('График 3: Вторая производная')

# График 4: Касательное расслоение
plt.figure(4)
tangent_lines_x_1 = np.linspace(a, b, 5)
for x_val in tangent_lines_x_1:
    tangent_line = f_prime_1(x_val) * (x_values_1 - x_val) + f_1(x_val)
    plt.plot(x_values_1, tangent_line, '--', label=f'Tangent at x={x_val}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График 4: Касательное расслоение')

# Выводим все графики
plt.show()

# Задаем интеграл для вычисления длины кривой
arc_length = integrate(sqrt(1 + diff(f_expr_1, x)**2), (x, a, b))

print(f"Длина кривой: {arc_length.evalf()}")