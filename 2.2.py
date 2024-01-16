def F(s):
    s1 = s.split()
    # Обратный порядок слов, объединение их в строку, и первая заглавная буква
    s2 = " ".join(reversed(s1)).capitalize()
    return s2

if __name__ == "__main__":   
    print("Output:", F(str(input("Input: "))))


# Работает верно