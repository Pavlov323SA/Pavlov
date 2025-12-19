def my_range(start, end, step):
    current = start
    while current < end:
        yield current
        current += step


if __name__ == "__main__":
    for i in my_range(1, 3, 0.5):
        print(i)