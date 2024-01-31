import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, CheckButtons, Button

# Параметры фигуры Лиссажу
amplitude_x, amplitude_y, phase_shift = 2, 3, np.pi / 4

# Функция Лиссажу с параметризацией угла
def lissajous_curve(amplitude_x, amplitude_y, phase_shift, theta_values):
    x = amplitude_x * np.sin(2 * theta_values)
    y = amplitude_y * np.sin(3 * theta_values + phase_shift)
    return x, y

def tangent_line_coefficients(amplitude_x, amplitude_y, phase_shift, theta):
    x, y = lissajous_curve(amplitude_x, amplitude_y, phase_shift, theta)
    dx_dtheta = 2 * amplitude_x * np.cos(2 * theta)
    dy_dtheta = 3 * amplitude_y * np.cos(3 * theta + phase_shift)
    slope = dy_dtheta / dx_dtheta
    intercept = y - slope * x
    return slope, intercept

# Обновление графика при изменении положения слайдера
def update_graph(val):
    global point, tangent_line, line
    theta = slider_position.val
    x, y = lissajous_curve(amplitude_x, amplitude_y, phase_shift, theta)

    point.set_data(x, y)

    if show_tangent:
        slope, intercept = tangent_line_coefficients(amplitude_x, amplitude_y, phase_shift, theta)
        tangent_line.set_data([x - 1, x + 1], [slope * (x - 1) + intercept, slope * (x + 1) + intercept])
    else:
        tangent_line.set_data([], [])

    fig.canvas.draw_idle()

# Сброс положения точки
def reset_point(val):
    slider_position.set_val(0)
    update_graph(0)

# Переключение отображения касательной
def toggle_tangent(label):
    global show_tangent
    show_tangent = not show_tangent
    update_graph(0)

# Изменение стиля линии фигуры Лиссажу
def change_line_style(label):
    line.set_linestyle(styles[label])
    fig.canvas.draw_idle()

# Изменение цвета линии фигуры Лиссажу
def change_line_color(label):
    line.set_color(colors[label])
    fig.canvas.draw_idle()

# Фиксированное начальное положение точки
initial_position = 0

# Генерация значений угла в диапазоне от 0 до 2*pi
theta_values = np.linspace(0, 2 * np.pi, 1000)
# Вычисление координат x и y для фигуры Лиссажу
x_values, y_values = lissajous_curve(amplitude_x, amplitude_y, phase_shift, theta_values)

# Построение графика
fig, ax = plt.subplots(figsize=(8, 6))
# Построение линии фигуры Лиссажу
(line,) = ax.plot(x_values, y_values, label="Лиссажу", linestyle="-", color="black")

# Отображение начальной точки
(point,) = ax.plot([], [], "ro", markersize=8)
(tangent_line,) = ax.plot([], [], "k--")

show_tangent = False

slider_position_ax = plt.axes([0.2, 0.01, 0.65, 0.03])
slider_position = Slider(slider_position_ax, "Расположение", 0, 2 * np.pi, valinit=initial_position, valstep=0.01)
slider_position.on_changed(update_graph)

reset_button_ax = plt.axes([0.85, 0.8, 0.1, 0.04])
reset_button = Button(reset_button_ax, "Сброс")
reset_button.on_clicked(reset_point)

tangent_checkbox_ax = plt.axes([0.85, 0.75, 0.1, 0.04])
tangent_checkbox = CheckButtons(tangent_checkbox_ax, ["Касательная"], actives=[False])
tangent_checkbox.on_clicked(toggle_tangent)

colors = {"Красный": "red", "Синий": "blue", "Оранжевый": "orange", "Желтый": "yellow"}
styles = {"-": "-", "--": "--", "-.": "-."}

radio_buttons_ax_color = plt.axes([0.85, 0.5, 0.1, 0.2])
radio_buttons_color = RadioButtons(radio_buttons_ax_color, list(colors.keys()))
radio_buttons_color.on_clicked(change_line_color)

radio_buttons_ax_style = plt.axes([0.85, 0.25, 0.1, 0.2])
radio_buttons_style = RadioButtons(radio_buttons_ax_style, list(styles.keys()))
radio_buttons_style.on_clicked(change_line_style)

update_graph(0)

if __name__ == "__main__":
    plt.show()
