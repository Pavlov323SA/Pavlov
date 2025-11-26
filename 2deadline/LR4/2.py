numbers = [25, 67, 42, 89, 13, 56, 78, 34, 91, 60]

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

big_numbers = []
for num in numbers:
    if num > 50:
        big_numbers.append(num)

print("Исходный список:", numbers)
print("Четные числа:", even_numbers)
print("Числа больше 50:", big_numbers)