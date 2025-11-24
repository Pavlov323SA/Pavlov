count = int(input("Сколько чисел вы хотите ввести? "))

numbers = []
for i in range(count):
    num = float(input(f"Введите число {i + 1}: "))
    numbers.append(num)

max_num = max(numbers)
min_num = min(numbers)
average = sum(numbers) / count

above_average = 0
for num in numbers:
    if num > average:
        above_average += 1

print("Результаты:")
print(f"Максимальное: {max_num}")
print(f"Минимальное: {min_num}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {above_average}")