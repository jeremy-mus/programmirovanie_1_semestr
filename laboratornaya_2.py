import time

def possibleMoves(x, y):
    # Функция возвращает множество возможных ходов для фигуры на доске с текущими координатами (x, y).

    moves = {
        (x - 3, y),
        (x - 2, y - 1), (x - 2, y + 1),
        (x - 1, y - 2), (x - 1, y), (x - 1, y + 2),
        (x, y - 3), (x, y - 1), (x, y + 1), (x, y + 3),
        (x + 1, y - 2), (x + 1, y), (x + 1, y + 2),
        (x + 2, y - 1), (x + 2, y + 1),
        (x + 3, y)
    }
    return moves

def figureDislocation(x, y, matrix):
    # Функция помечает текущую клетку (x, y) фигурой и обозначает возможные ходы фигуры на доске matrix.

    matrix[x][y] = '#'
    for i, j in possibleMoves(x, y):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix):
            matrix[i][j] = '*'
    return matrix

def otherFiguresDislocation(matrix, figures):
    # Функция помещает фигуры на доску matrix.
    
    for x, y in figures:
        figureDislocation(x, y, matrix)
    return matrix

def boardInitializer(N):
    # Функция инициализирует доску NxN, заполняя ее нулями.
    
    return [['0' for _ in range(N)] for _ in range(N)]

def boardPrinter(matrix):
    # Функция выводит текущее состояние доски в консоль.
    
    for row in matrix:
        print(" ".join(row))

def recursia(N, L, solutions, currentSolution, figureCount, startRow=0, startCol=0):
    # Рекурсивная функция для нахождения расстановок фигур на доске.

    if len(solutions) == 1:
        # Если уже найдено одно решение, завершаем рекурсию
        return

    if figureCount == L:
        # Проверяем, не добавлено ли уже текущее решение в множество решений
        if tuple(sorted(currentSolution)) not in solutions:
            solutions.add(tuple(sorted(currentSolution)))
            # Выводим доску с текущим решением в консоль
            boardPrinter(otherFiguresDislocation(boardInitializer(N), tuple(sorted(currentSolution))))
        return

    for i in range(startRow, N):
        for j in range(startCol if i == startRow else 0, N):
            # Проверяем, что текущая клетка не занята другой фигурой и нет пересечений с возможными ходами
            if all((moves not in currentSolution) for moves in possibleMoves(i, j)):
                # Добавляем текущую клетку в решение и рекурсивно вызываем функцию для следующей фигуры
                currentSolution.append((i, j))
                next_start_row = i if j == N - 1 else i
                next_start_col = j + 1 if j < N - 1 else 0
                recursia(N, L, solutions, currentSolution, figureCount + 1, next_start_row, next_start_col)
                # Отменяем последний выбор для backtracking
                currentSolution.pop()
                return  # Завершаем рекурсию после нахождения первого решения

if __name__ == "__main__":
    # Чтение входных данных из файла
    file = open("input.txt", "r")
    N, L, K = map(int, file.readline().split())

    figuresOnTheBoard = []
    solutions = set()

    # Чтение координат фигур из файла
    for line in file.readlines():
        x, y = map(int, line.split())
        figuresOnTheBoard.append((x, y))
    file.close()

    # Замер времени начала выполнения программы
    start_time = time.time()

    # Вызов рекурсивной функции для нахождения решений
    recursia(N, L, solutions, figuresOnTheBoard, 0)

    # Замер времени завершения выполнения программы
    end_time = time.time()

    print(f"Количество решений: {len(solutions)}")
    print(f"Время работы: {end_time - start_time}")

    # Если найдены решения, записываем их в файл
    if solutions:
        uniqueSolutions = {tuple(sorted(solution)) for solution in solutions}
        stringSolution = [" ".join(map(str, solution)) + "\n" for solution in uniqueSolutions]
        with open("output.txt", "w") as output_file:
            output_file.writelines(stringSolution)
    else:
        print("no solutions")
