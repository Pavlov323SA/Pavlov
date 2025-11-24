n = int(input("Введите число n: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Сумма чисел от 1 до {n}: {total}")
