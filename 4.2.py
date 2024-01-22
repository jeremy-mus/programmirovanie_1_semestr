def Permutations(n):
    # Если входной список пуст, возвращаем список, содержащий один пустой список
    if not n:
        return [[]]
    result = []

    for i in range(len(n)):
        newList = n[i]
        neitherNums = n[:i] + n[i + 1:]

    # Рекурсивный вызов Permutations для оставшихся элементов
        for i in Permutations(neitherNums):
            result.append([newList] + i)

    return result

if __name__ == "__main__":
    print("Output:", Permutations(list(map(int, input("Input: ")[1:-1].split(",")))))

# Работает верно
