import time
def possibleMoves(x, y):
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
    matrix[x][y] = '#'
    for i, j in possibleMoves(x, y):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix):
            matrix[i][j] = '*'
    return matrix


def otherFiguresDislocation(matrix, figures):
    for x, y in figures:
        figureDislocation(x, y, matrix)
    return matrix


def boardInitializer(N):
    return [['0' for _ in range(N)] for _ in range(N)]


def print_board(matrix):
    for row in matrix:
        print(" ".join(row))


def recursia(N, L, solutions, currentSolution, figureCount):
    if figureCount == L:
        if tuple(sorted(currentSolution)) not in solutions:
            solutions.add(tuple(sorted(currentSolution)))
            print_board(otherFiguresDislocation(boardInitializer(N), tuple(sorted(currentSolution))))
        return

    for i in range(N):
        for j in range(N):
            if all((moves not in currentSolution) for moves in possibleMoves(i, j)):
                currentSolution.append((i, j))
                recursia(N, L, solutions, currentSolution, figureCount + 1)
                currentSolution.pop()


if __name__ == "__main__":
    file = open("input.txt", "r")
    N, L, K = map(int, file.readline().split())

    figuresOnTheBoard = []
    solutions = set()

    for line in file.readlines():
        x, y = map(int, line.split())
        figuresOnTheBoard.append((x, y))
    file.close()

    start_time = time.time()
    recursia(N, L, solutions, figuresOnTheBoard, 0)
    end_time = time.time()


    print(f"Колличество решений: {len(solutions)}")
    print(f"Время работы: {end_time - start_time}")

    if solutions:
        uniqueSolutions = {tuple(sorted(solution)) for solution in solutions}
        stringSolution = [" ".join(map(str, solution)) + "\n" for solution in uniqueSolutions]
        with open("output.txt", "w") as output_file:
            output_file.writelines(stringSolution)
    else:
        print("no solutions")