def sum_digits(number):
    if number == 0:
        return 0
    return (number % 10) + sum_digits(number // 10)


if __name__ == "__main__":
    print(sum_digits(12345))