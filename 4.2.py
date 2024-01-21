from itertools import permutations

def Permutations(n):
    # Создаем множество уникальных перестановок и преобразуем его в список списков
    return list(map(list, set(permutations(n))))

if __name__ == "__main__":
    # Выводим результат, запрашивая ввод пользователя в виде строки и преобразуем в список целых чисел
    print("Output:", Permutations(list(map(int, input("Input: ")[1:-1].split(",")))))


# Работает верно
