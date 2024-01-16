def both(a, b):
    # Находим пересечение множеств
    c = set(a) & set(b)
    
    # Формируем строку результата с учетом количества элементов
    if len(c) % 10 in [1, 2, 3, 4]:
        return f"1) {len(c)} элемента: {c}"
    else:
        return f"1) {len(c)} элементов: {c}"

def neither(a, b):
    # Находим симметрическую разность множеств
    c = set(a) ^ set(b)
    
    # Формируем строку результата с учетом количества элементов
    if len(c) % 10 in [1, 2, 3, 4]:
        return f"2) {len(c)} элемента: {c}"
    else:
        return f"2) {len(c)} элементов: {c}"

def firstOriginal(a, b):
    # Находим элементы, присутствующие только в первом списке
    c = list(set(a) - set(b))
    
    # Формируем строку результата с учетом количества элементов
    if len(c) % 10 in [1, 2, 3, 4]:
        return f"3) {len(c)} элемента: {c}"
    else:
        return f"3) {len(c)} элементов: {c}"

def secondOriginal(a, b):
    # Находим элементы, присутствующие только во втором списке
    c = list(set(b) - set(a))
    
    # Формируем строку результата с учетом количества элементов
    if len(c) % 10 in [1, 2, 3, 4]:
        return f"4) {len(c)} элемента: {c}"
    else:
        return f"4) {len(c)} элементов: {c}"

if __name__ == "__main__":
    x = input("list1: ")
    y = input("list2: ")

    a = [int(i) for i in x[1:-1].split(", ")]
    b = [int(i) for i in y[1:-1].split(", ")]

    print(both(a, b))
    print(neither(a, b))
    print(firstOriginal(a, b))
    print(secondOriginal(a, b))


# Работает верно