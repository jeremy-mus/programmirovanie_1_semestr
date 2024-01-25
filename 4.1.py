def numberSum(n, c):
    n.sort()

    result = None

    for i in range(len(n) - 3):
        left, right = i + 1, len(n) - 1  # Устанавливаем указатели left и right

        # Ищем сумму четырех чисел, близкую к целевой сумме c
        while left < right:
            nSum = n[i] + n[left] + n[right] + n[left+1]

            # Если результат пуст или текущая сумма ближе к цели, чем предыдущая, обновляем результат
            if result is None or abs(nSum - c) < abs(sum(result) - c):
                result = [n[i], n[left], n[right], n[left+1]]

            # Перемещаем указатели left и right в зависимости от текущей суммы
            if nSum < c:
                left += 1
            else:
                right -= 1

    return result, sum(result)

if __name__ == "__main__":
    print("Output:", numberSum([int(x) for x in input("List: ").replace('[', '').replace(']', '').split(',')], int(input("c: "))))
