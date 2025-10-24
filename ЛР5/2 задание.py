a, b, c = map(int, input("Введите три целых числа через пробел: ").split())

mult1 = a * b
mult2 = b * c
mult3 = c * a

pow_result = a ** 4
mod_result = b % c
div_result = c // a

print("Результаты умножения:")
print("a * b =", mult1)
print("b * c =", mult2)
print("c * a =", mult3)

print("\nРезультаты дополнительных операций:")
print("a в 4 степени =", pow_result)
print("Остаток от деления b на c =", mod_result)
print("Целочисленное деление c на a =", div_result)

print("\nСумма результатов из пункта 5 =", pow_result + mod_result + div_result)