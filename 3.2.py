def weirdMatrix(a):
    # Перестановка элементов внутри каждой строки относительно главной диагонали
    for i in range(1, len(a)):
        k = 1
        while True:
            if k > i:
                break
            a[i-k][i], a[i][i-k] = a[i][i-k], a[i-k][i]
            k += 1

    # Переворот матрицы относительно её середины (по горизонтали)
    for j in range(len(a)//2):
        a[j], a[len(a) - j - 1] = a[len(a) - j - 1], a[j]
    
    return a

if __name__ == "__main__":   
    print("Output:", weirdMatrix(eval(input("Input: "))))



# Работает верно