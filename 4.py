text = input("Введите текст: ")
range_input = input("Введите диапазон: ").split()
start = int(range_input[0]) - 1
end = int(range_input[1])
result = text[start:end]
print(result)