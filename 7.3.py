def get_pins(n):
    # Словарь с близлежащими цифрами для каждой цифры на клавиатуре
    a = {'0': ['0', '8'], '1': ['1', '2', '4'], '2': ['1', '2', '3', '5'], '3': ['2', '3', '6'], '4': ['1', '4', '5', '7'], '5': ['2', '4', '5', '6', '8'], '6': ['3', '5', '6', '9'], '7': ['4', '7', '8'], '8': ['0', '5', '7', '8', '9'], '9': ['6', '8', '9']}

    if not n:
        return []

    b = a[n[0]]
    for i in n[1:]:
        # Генерация комбинаций для текущей цифры, основываясь на предыдущих значениях b
        b = [x + y for x in b for y in a[i]]

    return b

if __name__ == "__main__":
    print("Output:", get_pins(input("Input: ")))

# Работает верно