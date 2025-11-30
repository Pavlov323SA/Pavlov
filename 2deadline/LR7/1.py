def sum_numbers(*numbers: int | float) -> int | float:
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4, 5))
print(sum_numbers(10, 20))
print(sum_numbers(2.5, 3.7, 1.8))
