def groups(n):
    a = []
    for i in n:
        # Флаг для обозначения того, была ли найдена группа для текущей строки
        T = False
        
        # Итерация по каждой группе в результате
        for j in a:
            if sorted(i) == sorted(j[0]) and len(i) == len(j[0]):
                j.append(i)
                T = True
                break
        
        # Если не было найдено существующей группы, создаем новую
        if not T:
            a.append([i])

    return a

if __name__ == "__main__":
    print("Output:", groups(list(input("Input: "))))


# Работает верно