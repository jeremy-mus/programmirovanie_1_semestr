from itertools import permutations

def Permutations(n):
    # Используем множество для избежания дубликатов, затем преобразуем результат в список
    a = list(set(permutations(n)))
    return a

if __name__ == "__main__":
    print("Output:", Permutations(list(input("Input: "))))


# Работает верно