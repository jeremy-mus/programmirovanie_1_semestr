def palindrom(n):
    # Сохраняем оригинальное значение числа
    n1 = n
    # Создаем переменную для обратного числа
    n2 = 0
    if n < 0:
        return False
    # Используем цикл для создания обратного числа
    while n > 0:
        n2 = n2 * 10 + n % 10
        n = n // 10
    return n1 == n2

if __name__ == "__main__":   
    print("Output:", palindrom(int(input("Input: "))))


# Работает верно