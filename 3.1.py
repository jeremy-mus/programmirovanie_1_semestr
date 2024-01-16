def reverseMatrix(a):
    # Создание списка для хранения результатов
    j = []

    while len(a) != 0:
        # Обработка верхней строки матрицы
        for i in range(len(a[0])):
            j.append(a[0][i])
        a.remove(a[0]) 

        # Обработка правого столбца матрицы
        if a and a[0]:
            for l in range(len(a)):
                j.append(a[l][-1])
                a[l].pop()

        # Обработка нижней строки матрицы
        if a:
            for m in range(len(a[-1])-1, -1, -1):
                j.append(a[-1][m])  
            a.pop()

        # Обработка левого столбца матрицы
        if a and a[0]:
            for n in range(len(a)-1, -1, -1):
                j.append(a[n][0])
                a[n].pop(0)

    return j

if __name__ == "__main__":   
    print("Output:", reverseMatrix(eval(input("Input: matrix = "))))


# Работает верно