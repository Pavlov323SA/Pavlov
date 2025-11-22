import math

data = input("Введите число1 знак число2: ").split()
num1 = float(data[0])
operator = data[1]
num2 = float(data[2])

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль"
elif operator == "%":
    result = num1 % num2
elif operator == "//":
    if num2 != 0:
        result = num1 // num2
    else:
        result = "Ошибка: деление на ноль"
elif operator == "**":
    result = num1 ** num2
elif operator == "%%":
    result = num1 * num2 / 100
elif operator == "/**":
    if num1 >= 0:
        result = math.sqrt(num1)
    else:
        result = "Ошибка: корень из отрицательного числа"
else:
    result = "Неизвестная операция"

print(f"Результат: {result}")