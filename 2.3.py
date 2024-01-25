def brackets(n):
    # Функция проверяет, имеет ли строка сбалансированные скобки.
    stack = []
    bracketsVariants = {"(": ")", "[": "]", "{": "}"}

    for i in n:        
        if i in bracketsVariants.keys():
            # Если символ = открывающая скобка, добавляем ее в стек.
            stack.append(i)
        elif i in bracketsVariants.values():
            # Если символ = закрывающая скобка.
            if not stack or bracketsVariants[stack.pop()] != i:
                # Если стек пуст или последняя открытая скобка не соответствует текущей закрывающей, возвращаем False.
                return False
            
    # Проверка, что стек пуст после обхода строки.
    return len(stack) == 0


def longestStr(n):    
    maxStr = ""
    a = 0

    if brackets(n):
        # Если вся строка имеет сбалансированные скобки, возвращаем True.
        return True
    else:
        for i in range(len(n) - 1):            
            for j in range(i + 1, len(n)):                
                if brackets(n[i:j]):
                    if a < len(n[i:j]):
                        # Если текущая подстрока длиннее сохраненной, обновляем переменные.
                        a = len(n[i:j])
                        maxStr = n[i:j]

        if maxStr:
            return maxStr
        else:
            return False

if __name__ == "__main__":
    print("Output:", longestStr(input("Input: ")))