def F(s, n):
    # Если n равно 1 или больше или равно длине строки s, возвращаем исходную строку s
    if n == 1 or n >= len(s):
        return s

    a = [""] * n
    index = 0
    step = 1

    for i in s:
        # Добавляем текущий символ к текущей строке
        a[index] += i

        # Определяем следующий индекс строки и шаг
        if index == 0:
            # Если достигнут верхний конец зигзага, меняем шаг на 1 (движение вниз)
            step = 1
        elif index == n - 1:
            # Если достигнут нижний конец зигзага, меняем шаг на -1 (движение вверх)
            step = -1

        index += step

    return "".join(a)

if __name__ == "__main__":
    print("Output:", F(input("Input string: "), int(input("Input num: "))))
