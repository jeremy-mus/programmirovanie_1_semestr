def recursia(a, s):
    # Замена пробелов на знаки "+" и "-" с дальнейшей проверкой
    if a.count(" ") > 0:
        result_plus = recursia(a.replace(" ", "+", 1), s)
        if result_plus:
            return result_plus
        result_minus = recursia(a.replace(" ", "-", 1), s)
        if result_minus:
            return result_minus
        return None
    
    operator = ""
    num = 0
    currentNumber = ""

    for i in a:
        if i in {"+", "-"}:
            operator = i
        else:
            currentNumber += i
            continue

        # Преобразование текущего числа в целое число и обновление переменной num
        newNum = int(currentNumber)
        if operator == "+":
            num += newNum
        elif operator == "-":
            num -= newNum
        currentNumber = ""

    # Последнее число после последнего знака
    if currentNumber:
        newNum = int(currentNumber)
        if operator == "+":
            num += newNum
        elif operator == "-":
            num -= newNum

    if num == s:
        return f"{a} = {s}"

def main():
    with open("laboratornaya_1.txt", "r") as file:
        q = file.readline()
        a = list(map(int, q.split()))
        s = a.pop()
        # Получение строки начиная с индекса 1-го пробела и заканчивая индексом последнего
        q = q[q.find(" ")+1:q.rfind(" ")]
        
        result = recursia(q, s)
        # Запись результата в тот же файл, с которого происходило считывание
        if result:
            print(result)
            with open("laboratornaya_1.txt", "w", encoding="utf-8") as output_file:
                output_file.write(result)
        else:
            print("no solution")
            with open("laboratornaya_1.txt", "w", encoding="utf-8") as output_file:
                output_file.write("no solution")

if __name__ == "__main__":
    main()

# Работает верно
