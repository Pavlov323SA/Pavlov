N = int(input("Введите количество чисел: "))

numbers = []
for i in range(N):
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)

total_sum = 0
for num in numbers:
    total_sum += num

average = total_sum / N

print(f"Среднее арифметическое: {average}")