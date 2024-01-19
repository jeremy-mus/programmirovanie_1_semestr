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
    
    if eval(a) == s:
        return (f"{a} = {s}")

def main():
    with open("laboratornaya_1.txt", "r", encoding = "utf-8") as file:
        temp = file.readline()
        a = list(map(int, temp.split()))
        s = a.pop()
        # Получение строки начиная с индекса 1-го пробела и заканчивая индексом последнего
        temp = temp[temp.find(" ")+1:temp.rfind(" ")]
        
        result = recursia(temp, s)
        
        if result:
            print(result)
        else:
            print("no solution")

if __name__ == "__main__":
    main()

# Работает верно
