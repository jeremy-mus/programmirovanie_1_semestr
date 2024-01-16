def setVariants(n):
    # Извлекаем уникальные элементы из входного списка
    a = list(set(n))
    # Создаем список для хранения подмножеств
    b = [[]]

    for i in a:
        l = [x + [i] for x in b]
        b.extend(l)

    return len(b) - 1, b[1:]

if __name__ == "__main__":   
    a, b = setVariants(eval(input("list = ")))
    
    print("Подмножества: ", b)
    print("Количество подмножеств: ", a)


# Работает верно