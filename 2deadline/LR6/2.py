def simple_calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль!"
    else:
        return "Ошибка: неверный оператор!"

result = simple_calculator(10, 5, '*')
print(result)